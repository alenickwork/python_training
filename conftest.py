import pytest
from fixture.application import Application
from fixture.session import SessionBroken


fixture = None

@pytest.fixture(scope="class")
def app(request):
    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        url = request.config.getoption("--url")
        fixture = Application(browser, url)
        fixture.session.login(username = "admin",
                  password = "secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(username="admin",
                                  password="secret")
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
    parser.addoption("--url", action="store", default="http://localhost/addressbook/")