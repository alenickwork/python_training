addressbook_url = "http://localhost/addressbook/"

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SessionHelper:

    def __init__(self,app):
        self.app = app

    def _open_addressbook(self):
        self.app.wd.get(addressbook_url)

    def login(self, username, password):
        self._open_addressbook()
        print("Login")
        self.app.page_objects.text_input("user", username)
        self.app.page_objects.text_input("pass", password)
        self.app.page_objects.input_click("Login")

    def logout(self):
        print("Logout")
        self.app.page_objects.link_click("Logout")
        wait = WebDriverWait(self.app.wd, 10)
        wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm')))
