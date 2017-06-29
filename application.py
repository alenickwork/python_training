# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

addressbook_url = "http://localhost/addressbook/"

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def destroy(self):
        self.wd.quit()

    def create_new_contact(self, contact_data):
        print("Go to add new")
        self.wd.find_element_by_link_text("add new").click()
        self.input_contact_data(contact_data)
        self.contact_submit()

    def create_new_group(self, group_data):
        self.open_groups_page()
        self.click_new_group()
        self.input_group_data(group_data)
        self.submit()
        self.return_to_groups_page()

    def open_groups_page(self):
        self.wd.find_element_by_link_text("groups").click()

    def click_new_group(self):
        self.wd.find_element_by_name("new").click()


    def return_to_groups_page(self):
        self.open_groups_page()


    def submit(self):
        self.wd.find_element_by_name("submit").click()


    def input_group_data(self,group_data):
        print("Input group data")
        # input group data
        self._text_element_input(field_name="group_name", value=group_data.name)
        self._text_element_input(field_name="group_header", value=group_data.header)
        self._text_element_input(field_name="group_footer", value=group_data.footer)

    def input_contact_data(self, contact_data):
        print("Input contact data")
        self._text_element_input(field_name="firstname", value=contact_data.firstname)
        self._text_element_input(field_name="middlename", value=contact_data.middlename)
        self._text_element_input(field_name="lastname", value=contact_data.lastname)
        self._text_element_input(field_name="nickname", value=contact_data.nickname)
        self._file_element_input(field_name="photo", value=contact_data.photo_link)
        self._text_element_input(field_name="title", value=contact_data.title)
        self._text_element_input(field_name="company", value=contact_data.company)
        self._text_element_input(field_name="address", value=contact_data.address)
        self._text_element_input(field_name="home", value=contact_data.home_phone)
        self._text_element_input(field_name="mobile", value=contact_data.mobile_phone)
        self._text_element_input(field_name="work", value=contact_data.work_phone)
        self._text_element_input(field_name="fax", value=contact_data.fax)
        self._text_element_input(field_name="email", value=contact_data.email_prior)
        self._text_element_input(field_name="email2", value=contact_data.email_2)
        self._text_element_input(field_name="email3", value=contact_data.email_3)
        self._text_element_input(field_name="homepage", value=contact_data.homepage)
        self._dropdown_element_input(field_name="bday", value=contact_data.birthday_day)
        self._dropdown_element_input(field_name="bmonth", value=contact_data.birthday_month)
        self._text_element_input(field_name="byear", value=contact_data.birthday_year)
        self._dropdown_element_input(field_name="aday", value=contact_data.anniversary_day)
        self._dropdown_element_input(field_name="amonth", value=contact_data.anniversary_month)
        self._text_element_input(field_name="ayear", value=contact_data.anniversary_year)
        self._text_element_input(field_name="address2", value=contact_data.address_secondary)
        self._text_element_input(field_name="phone2", value=contact_data.phone_secondary)
        self._text_element_input(field_name="notes", value=contact_data.notes)

    def login(self, username, password):
        self._open_addressbook()
        print("Login")
        self._text_element_input("user", username)
        self._text_element_input("pass", password)
        self.wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def _open_addressbook(self):
        self.wd.get(addressbook_url)

    def logout(self):
        print("Logout")
        self.wd.find_element_by_id("content").click()
        self.wd.find_element_by_link_text("Logout").click()

    def contact_submit(self):
        print("Click Enter")
        self.wd.find_element_by_name("submit").click()

    def _dropdown_element_input(self, field_name, value):
        print("\tdrop-down <{1}> |\tvalue <{0}>".format(value, field_name))
        select = Select(self.wd.find_element_by_name(field_name))
        select.select_by_visible_text(value)

    def _file_element_input(self, field_name, value):
        print("\tfile upload <{1}> |\tvalue <{0}>".format(value, field_name))
        self.wd.find_element_by_name(field_name).send_keys(value)

    def _text_element_input(self, field_name, value):
        print("\ttext input <{1}> |\tvalue <{0}>".format(value, field_name))
        self.wd.find_element_by_name(field_name).click()
        self.wd.find_element_by_name(field_name).clear()
        self.wd.find_element_by_name(field_name).send_keys(value)
