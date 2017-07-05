addressbook_url = "http://localhost/addressbook/"

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