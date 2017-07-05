# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"

from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.pageObjects import PageObjectsHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.page_objects = PageObjectsHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.wd.quit()







