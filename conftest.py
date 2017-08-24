import pytest
from fixture.application import Application
from fixture.session import SessionBroken
import json
import os

fixture = None
target = None

@pytest.fixture(scope="class")
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),request.config.getoption("--target"))
    if target is None:
        with open(config_file_path) as config_file:
            target = json.load(config_file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser, target["baseUrl"])
        fixture.session.login(username = target["username"],
                              password = target["password"])
    return fixture

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
