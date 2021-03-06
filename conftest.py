import pytest
from fixture.application import Application
from fixture.session import SessionBroken
from fixture.db import DbFixture
from fixture.orm import ORMFixture
import json
import jsonpickle
import os
import importlib

fixture = None
target = None

def load_config(file):
    global target
    if target is None:
        config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                        file)
        with open(config_file_path) as config_file:
            target = json.load(config_file)
    return target

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")

@pytest.fixture(scope="class")
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, web_config["baseUrl"])
        fixture.session.login(username = web_config["username"],
                              password = web_config["password"])
    return fixture

@pytest.fixture(scope="session")
def orm(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    ormfixture = ORMFixture(host = db_config['host'],
                          name = db_config['name'],
                          user = db_config['user'],
                          password = db_config['password'])
    return ormfixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host = db_config['host'],
                          name = db_config['name'],
                          user = db_config['user'],
                          password = db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse = True)
def stop(request):
    def fin():
        try:
            fixture.session.ensure_logout()
            fixture.destroy()
        except SessionBroken:
            pass
    request.addfinalizer(fin)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])
        if fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids = [str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_from_json(jfile):
    file_p = os.path.join(os.path.dirname(os.path.abspath(__file__)),"data/%s.json" % jfile)
    with open(file_p) as jfile_cont:
        return jsonpickle.decode(jfile_cont.read())
