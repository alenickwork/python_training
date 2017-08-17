import pytest
from fixture.application import Application
from fixture.session import SessionBroken

fixture = None

@pytest.fixture(scope="class")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
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
