from selenium.webdriver.support.ui import Select

class PageObjectsHelper:

    def __init__(self,app):
        self.app = app

    def dropdown_select(self, field_name, value):
        print("\tdrop-down <{1}> |\tvalue <{0}>".format(value, field_name))
        select = Select(self.app.wd.find_element_by_name(field_name))
        select.select_by_visible_text(value)

    def file_select(self, field_name, value):
        print("\tfile upload <{1}> |\tvalue <{0}>".format(value, field_name))
        self.app.wd.find_element_by_name(field_name).send_keys(value)

    def text_input(self, field_name, value):
        print("\ttext input <{1}> |\tvalue <{0}>".format(value, field_name))
        self.app.wd.find_element_by_name(field_name).click()
        self.app.wd.find_element_by_name(field_name).clear()
        self.app.wd.find_element_by_name(field_name).send_keys(value)

    def button_click(self, button_name):
        self.app.wd.find_element_by_name(button_name).click()

    def input_click(self, input_value):
        self.app.wd.find_element_by_xpath("//input[@value='{0}']".format(input_value)).click()

    def link_click(self, link_text):
        self.app.wd.find_element_by_link_text(link_text).click()

    def menu_item_click(self, menu_name):
        print("Menu item name:{0} click".format(menu_name))
        self.app.wd.find_element_by_name(menu_name).click()

    def submit(self):
        self.button_click("submit")

    def update(self):
        self.button_click("update")

