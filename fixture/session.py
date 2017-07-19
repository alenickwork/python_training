addressbook_url = "http://localhost/addressbook/"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fixture.actions import ActionsHelper

class SessionHelper(ActionsHelper):

    def __init__(self,app):
        super(SessionHelper,self).__init__(app)
        self.app = app

    def _open_addressbook(self):
        self.app.wd.get(addressbook_url)

    def login(self, username, password):
        self._open_addressbook()
        print("Login")
        self.text_input("user", username)
        self.text_input("pass", password)
        self.input_click("Login")

    def logout(self):
        print("Logout")
        self.link_click("Logout")
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm')))
