from fixture.actions import ActionsHelper

from model.contact import Contact

import contextlib
import time
import re
# from selenium.webdriver import Remote
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support.expected_conditions import staleness_of


class ContactHelper(ActionsHelper):

    # @contextlib.contextmanager
    # def wait_for_page_load(self):
    #     timeout = 6
    #     wd = self.app.wd
    #     old_page = wd.find_element_by_xpath("//input[@value='Enter']")
    #     yield
    #     WebDriverWait(self, timeout).until(staleness_of(old_page))

    # @contextlib.contextmanager
    # def wait_for_init_page_load(self):
    #     timeout = 6
    #     wd = self.app.wd
    #     yield
    #     while not wd.getCurrentUrl().endswith("addressbook/"):
    #         time.sleep(3)


    def __init__(self,app):
        super(ContactHelper,self).__init__(app)
        self.app = app
        self.wd = app.wd

    @property
    def page_is_opened(self):
        wd = self.app.wd
        return len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0


    def force_open_contacts_page(self):
        print("Open contacts page")
        self.link_click("home")
        self.wait_button_clickable("Send e-Mail")

    def open_contacts_page(self):
        if not self.page_is_opened:
            print("Open contacts page")
            self.link_click("home")
            self.wait_button_clickable("Send e-Mail")

    def return_to_contacts_page(self):
        self.open_contacts_page()

    def create(self, contact_data):
        print("Create new contact")
        self.open_contacts_page()
        self._click_new()
        self._enter_data(contact_data)
        self.submit()
        self.contact_cache = None

    @property
    def count(self):
        wd = self.app.wd
        tmp = len(wd.find_elements_by_xpath("//td[@class='center']/input[@type='checkbox']"))
        print("{0} Contacts found".format(tmp))
        return tmp

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_id(self, id = 0):
        print("Delete contact #{0}".format(id))
        self.open_contacts_page()
        self.select_by_id(id)
        self.input_click("Delete")
        self.wd.switch_to_alert().accept()
        time.sleep(3)
        self.return_to_contacts_page()
        self.contact_cache = None


    def delete_by_index(self, index = 0):
        print("Delete contact #{0}".format(index))
        self.open_contacts_page()
        self.select_by_index(index)
        self.input_click("Delete")
        self.wd.switch_to_alert().accept()
        time.sleep(3)
        self.return_to_contacts_page()
        self.contact_cache = None

    def select_by_index(self, index):
        wd = self.app.wd
        to_del = wd.find_elements_by_xpath("//td[@class='center']/input[@type='checkbox']")[index]
        if not to_del.is_selected():
            to_del.click()
        return to_del

    def select_by_id(self, id):
        wd = self.app.wd
        to_del = wd.find_element_by_css_selector("input[id='%s']" % id)
        if not to_del.is_selected():
            to_del.click()
        return to_del

    def delete(self, contact_data):
        print("Delete contact {0} {1}".format(contact_data.firstname, contact_data.lastname))
        self.open_contacts_page()
        to_del = self.wd.find_element_by_xpath(contact_data.xpath.checkbox)
        if not to_del.is_selected():
            to_del.click()
        self.input_click("Delete")
        self.wd.switch_to_alert().accept()
        time.sleep(3)
        self.wait_button_clickable("Delete")
        self.return_to_contacts_page()
        self.contact_cache = None

    def modify(self, contact_data, new_contact_data):
        print("Modify contact {0} {1}".format(contact_data.firstname, contact_data.lastname))
        self.open_contacts_page()
        to_mod = self.wd.find_element_by_xpath(contact_data.xpath.edit)
        to_mod.click()
        self._enter_data(new_contact_data)
        self.input_click("Update")
        self.return_to_contacts_page()
        self.contact_cache = None

    def modify_first(self, new_contact_data):
        print("Modify first contact")
        self.open_contacts_page()
        to_mod = self.wd.find_element_by_xpath("//td[@class ='center']/a[contains(@href,'edit')]")
        to_mod.click()
        self._enter_data(new_contact_data)
        self.input_click("Update")
        self.return_to_contacts_page()

    def modify_by_index(self, index, new_contact_data):
        print("Modify contact #{0}".format(index))
        self.open_contacts_page()
        self.open_contact_edit_by_index(index)
        self._enter_data(new_contact_data)
        self.input_click("Update")
        self.return_to_contacts_page()

    def modify_by_id(self, id, new_contact_data):
        print("Modify contact #{0}".format(id))
        self.open_contacts_page()
        self.open_contact_edit_by_id(id)
        self._enter_data(new_contact_data)
        self.input_click("Update")
        self.return_to_contacts_page()

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        to_mod = wd.find_elements_by_xpath("//td[@class ='center']/a[contains(@href,'edit')]")[index]
        to_mod.click()
        return to_mod

    def open_contact_edit_by_id(self, id):
        wd = self.app.wd
        to_mod = wd.find_element_by_xpath(".//tr[td[input[@id='%s']]]/td[a[contains(@href,'edit')]]" % id)
        to_mod.click()
        return to_mod


    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        to_mod = self.wd.find_elements_by_xpath("//td[@class ='center']/a[contains(@href,'view')]")[index]
        to_mod.click()
        return to_mod


    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                id = cells[0].find_element_by_tag_name("input").get_attribute('value')
                all_phones = cells[5].text#.splitlines()
                all_mails = cells[4].text  # .splitlines()
                tmp_cont = Contact(lastname = lastname, firstname = firstname, id = id,
                                   all_phones_from_homepage = all_phones,
                                   all_mails_from_homepage=all_mails
                                   )
                self.contact_cache.append(tmp_cont)
        return self.contact_cache

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)

        tmp =  Contact(firstname = wd.find_element_by_name('firstname').get_attribute('value'),
                       lastname = wd.find_element_by_name('lastname').get_attribute('value'),
                       id = wd.find_element_by_name('id').get_attribute('value'),
                       home_phone = wd.find_element_by_name('home').get_attribute('value'),
                       work_phone=wd.find_element_by_name('work').get_attribute('value'),
                       mobile_phone=wd.find_element_by_name('mobile').get_attribute('value'),
                       phone_secondary=wd.find_element_by_name('phone2').get_attribute('value'),
                       email_prior=wd.find_element_by_name('email').get_attribute('value'),
                       email_2=wd.find_element_by_name('email2').get_attribute('value'),
                       email_3=wd.find_element_by_name('email3').get_attribute('value')
                       )
        self.return_to_contacts_page()

        return tmp

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        phone_secondary = re.search("P: (.*)", text).group(1)
        self.return_to_contacts_page()
        return Contact(home_phone = home_phone, work_phone=work_phone, mobile_phone=mobile_phone,
                       phone_secondary=phone_secondary)



    def _click_new(self):
        print("Go to add new")
        self.link_click("add new")
        self.wait_button_clickable("Enter")

    def _enter_data(self, contact_data):
        print("Input contact data")
        if contact_data.firstname is not None:
            self.text_input(field_name="firstname", value=contact_data.firstname)
        if contact_data.middlename is not None:
            self.text_input(field_name="middlename", value=contact_data.middlename)
        if contact_data.lastname is not None:
            self.text_input(field_name="lastname", value=contact_data.lastname)
        if contact_data.nickname is not None:
            self.text_input(field_name="nickname", value=contact_data.nickname)
        if contact_data.photo_link is not None:
            self.file_select(field_name="photo", value=contact_data.photo_link)
        if contact_data.title is not None:
            self.text_input(field_name="title", value=contact_data.title)
        if contact_data.company is not None:
            self.text_input(field_name="company", value=contact_data.company)
        if contact_data.address is not None:
            self.text_input(field_name="address", value=contact_data.address)
        if contact_data.home_phone is not None:
            self.text_input(field_name="home", value=contact_data.home_phone)
        if contact_data.mobile_phone is not None:
            self.text_input(field_name="mobile", value=contact_data.mobile_phone)
        if contact_data.work_phone is not None:
            self.text_input(field_name="work", value=contact_data.work_phone)
        if contact_data.fax is not None:
            self.text_input(field_name="fax", value=contact_data.fax)
        if contact_data.email_prior is not None:
            self.text_input(field_name="email", value=contact_data.email_prior)
        if contact_data.email_2 is not None:
            self.text_input(field_name="email2", value=contact_data.email_2)
        if contact_data.email_3 is not None:
            self.text_input(field_name="email3", value=contact_data.email_3)
        if contact_data.homepage is not None:
            self.text_input(field_name="homepage", value=contact_data.homepage)
        if contact_data.birthday_day is not None:
            self.dropdown_select(field_name="bday", value=contact_data.birthday_day)
        if contact_data.birthday_month is not None:
            self.dropdown_select(field_name="bmonth", value=contact_data.birthday_month)
        if contact_data.birthday_year is not None:
            self.text_input(field_name="byear", value=contact_data.birthday_year)
        if contact_data.anniversary_day is not None:
            self.dropdown_select(field_name="aday", value=contact_data.anniversary_day)
        if contact_data.anniversary_month is not None:
            self.dropdown_select(field_name="amonth", value=contact_data.anniversary_month)
        if contact_data.anniversary_year is not None:
            self.text_input(field_name="ayear", value=contact_data.anniversary_year)
        if contact_data.address_secondary is not None:
            self.text_input(field_name="address2", value=contact_data.address_secondary)
        if contact_data.phone_secondary is not None:
            self.text_input(field_name="phone2", value=contact_data.phone_secondary)
        if contact_data.notes is not None:
            self.text_input(field_name="notes", value=contact_data.notes)