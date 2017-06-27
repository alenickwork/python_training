# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #3: add new contact
"""
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

import unittest

from contact_single_fields import Contact
import os

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):

    addressbook_url = "http://localhost/addressbook/"

    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_contact(self):
        success = True
        wd = self.wd

        self.open_addressbook(wd)

        self.login(wd, username = "admin",
                       password = "secret")

        self.create_new_contact(wd, Contact(firstname = "test_fn",
                                            middlename = "test_mn",
                                            lastname = "test_ln",
                                            nickname = "test_nn",
                                            photo_link = os.path.join(os.path.dirname(__file__),
                                                                      "data",
                                                                      "Cute-White-Pigeon-Display-Picture.jpg"),
                                            title = "test_title",
                                            company = "test_c",
                                            address = "test_addr",
                                            home_phone = "test_hph",
                                            mobile_phone = "test_mph",
                                            work_phone = "test_wph",
                                            fax = "test_fx",
                                            email_prior = "test_em1",
                                            email_2 = "test_e2",
                                            email_3 = "test_e3",
                                            homepage = "test_hp",
                                            birthday_day = "15",
                                            birthday_month="March",
                                            birthday_year="1982",
                                            anniversary_day = "30",
                                            anniversary_month="April",
                                            anniversary_year="2011",
                                            address_secondary = "test_addr2",
                                            phone_secondary = "test_ph2",
                                            notes = "12121221")
                                )

        self.logout(wd)

        self.assertTrue(success)

    def create_new_contact(self, wd, contact_data):
        print("Go to add new")
        wd.find_element_by_link_text("add new").click()
        self.input_contact_data(wd, contact_data)
        self.contact_submit(wd)

    def input_contact_data(self, wd, contact_data):
        print("Input contact data")
        self._text_element_input(wd, field_name="firstname", value=contact_data.firstname)
        self._text_element_input(wd, field_name="middlename", value=contact_data.middlename)
        self._text_element_input(wd, field_name="lastname", value=contact_data.lastname)
        self._text_element_input(wd, field_name="nickname", value=contact_data.nickname)
        self._file_element_input(wd, field_name="photo", value=contact_data.photo_link)
        self._text_element_input(wd, field_name="title", value=contact_data.title)
        self._text_element_input(wd, field_name="company", value=contact_data.company)
        self._text_element_input(wd, field_name="address", value=contact_data.address)
        self._text_element_input(wd, field_name="home", value=contact_data.home_phone)
        self._text_element_input(wd, field_name="mobile", value=contact_data.mobile_phone)
        self._text_element_input(wd, field_name="work", value=contact_data.work_phone)
        self._text_element_input(wd, field_name="fax", value=contact_data.fax)
        self._text_element_input(wd, field_name="email", value=contact_data.email_prior)
        self._text_element_input(wd, field_name="email2", value=contact_data.email_2)
        self._text_element_input(wd, field_name="email3", value=contact_data.email_3)
        self._text_element_input(wd, field_name="homepage", value=contact_data.homepage)
        self._dropdown_element_input(wd, field_name="bday", value=contact_data.birthday_day)
        self._dropdown_element_input(wd, field_name="bmonth", value=contact_data.birthday_month)
        self._text_element_input(wd, field_name="byear", value=contact_data.birthday_year)
        self._dropdown_element_input(wd, field_name="aday", value=contact_data.anniversary_day)
        self._dropdown_element_input(wd, field_name="amonth", value=contact_data.anniversary_month)
        self._text_element_input(wd, field_name="ayear", value=contact_data.anniversary_year)
        self._text_element_input(wd, field_name="address2", value=contact_data.address_secondary)
        self._text_element_input(wd, field_name="phone2", value=contact_data.phone_secondary)
        self._text_element_input(wd, field_name="notes", value=contact_data.notes)

    def login(self, wd, username, password):
        print("Login")
        self._text_element_input(wd, "user", username)
        self._text_element_input(wd, "pass", password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_addressbook(self, wd):
        print("Open url")
        wd.get(self.addressbook_url)

    def logout(self, wd):
        print("Logout")
        wd.find_element_by_id("content").click()
        wd.find_element_by_link_text("Logout").click()

    def contact_submit(self, wd):
        print("Click Enter")
        wd.find_element_by_name("submit").click()

    def _dropdown_element_input(self, wd, field_name, value):
        print("\tdrop-down <{1}> |\tvalue <{0}>".format(value, field_name))
        select = Select(wd.find_element_by_name(field_name))
        select.select_by_visible_text(value)

    def _file_element_input(self, wd, field_name, value):
        print("\tfile upload <{1}> |\tvalue <{0}>".format(value, field_name))
        wd.find_element_by_name(field_name).send_keys(value)

    def _text_element_input(self, wd, field_name, value):
        print("\ttext input <{1}> |\tvalue <{0}>".format(value, field_name))
        wd.find_element_by_name(field_name).click()
        wd.find_element_by_name(field_name).clear()
        wd.find_element_by_name(field_name).send_keys(value)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
