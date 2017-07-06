class ContactHelper:

    def __init__(self,app):
        self.app = app

    def open_contacts_page(self):
        print("Open contacts page")
        self.app.page_objects.link_click("home")

    def return_to_contacts_page(self):
        self.open_contacts_page()

    def create(self, contact_data):
        print("Create new contact")
        self._click_new()
        self._enter_data(contact_data)
        self.app.page_objects.submit()

    def delete(self, contact_data):
        print("Delete contact {0} {1}".format(contact_data.firstname, contact_data.lastname))
        self.open_contacts_page()
        to_del = self.app.wd.find_element_by_xpath(contact_data.xpath.checkbox)
        if to_del is None:
            return None
        if not to_del.is_selected():
            to_del.click()
        self.app.page_objects.input_click("Delete")
        self.app.wd.switch_to_alert().accept()
        self.return_to_contacts_page()

    def modify(self, contact_data, new_contact_data):
        print("Modify contact {0} {1}".format(contact_data.firstname, contact_data.lastname))
        self.open_contacts_page()
        to_mod = self.app.wd.find_element_by_xpath(contact_data.xpath.edit)
        to_mod.click()
        self._enter_data(new_contact_data)
        self.app.page_objects.input_click("Update")
        self.return_to_contacts_page()

    def _click_new(self):
        print("Go to add new")
        self.app.page_objects.link_click("add new")

    def _enter_data(self, contact_data):
        print("Input contact data")
        if contact_data.firstname is not None:
            self.app.page_objects.text_input(field_name="firstname", value=contact_data.firstname)
        if contact_data.middlename is not None:
            self.app.page_objects.text_input(field_name="middlename", value=contact_data.middlename)
        if contact_data.lastname is not None:
            self.app.page_objects.text_input(field_name="lastname", value=contact_data.lastname)
        if contact_data.nickname is not None:
            self.app.page_objects.text_input(field_name="nickname", value=contact_data.nickname)
        if contact_data.photo_link is not None:
            self.app.page_objects.file_select(field_name="photo", value=contact_data.photo_link)
        if contact_data.title is not None:
            self.app.page_objects.text_input(field_name="title", value=contact_data.title)
        if contact_data.company is not None:
            self.app.page_objects.text_input(field_name="company", value=contact_data.company)
        if contact_data.address is not None:
            self.app.page_objects.text_input(field_name="address", value=contact_data.address)
        if contact_data.home_phone is not None:
            self.app.page_objects.text_input(field_name="home", value=contact_data.home_phone)
        if contact_data.mobile_phone is not None:
            self.app.page_objects.text_input(field_name="mobile", value=contact_data.mobile_phone)
        if contact_data.work_phone is not None:
            self.app.page_objects.text_input(field_name="work", value=contact_data.work_phone)
        if contact_data.fax is not None:
            self.app.page_objects.text_input(field_name="fax", value=contact_data.fax)
        if contact_data.email_prior is not None:
            self.app.page_objects.text_input(field_name="email", value=contact_data.email_prior)
        if contact_data.email_2 is not None:
            self.app.page_objects.text_input(field_name="email2", value=contact_data.email_2)
        if contact_data.email_3 is not None:
            self.app.page_objects.text_input(field_name="email3", value=contact_data.email_3)
        if contact_data.homepage is not None:
            self.app.page_objects.text_input(field_name="homepage", value=contact_data.homepage)
        if contact_data.birthday_day is not None:
            self.app.page_objects.dropdown_select(field_name="bday", value=contact_data.birthday_day)
        if contact_data.birthday_month is not None:
            self.app.page_objects.dropdown_select(field_name="bmonth", value=contact_data.birthday_month)
        if contact_data.birthday_year is not None:
            self.app.page_objects.text_input(field_name="byear", value=contact_data.birthday_year)
        if contact_data.anniversary_day is not None:
            self.app.page_objects.dropdown_select(field_name="aday", value=contact_data.anniversary_day)
        if contact_data.anniversary_month is not None:
            self.app.page_objects.dropdown_select(field_name="amonth", value=contact_data.anniversary_month)
        if contact_data.anniversary_year is not None:
            self.app.page_objects.text_input(field_name="ayear", value=contact_data.anniversary_year)
        if contact_data.address_secondary is not None:
            self.app.page_objects.text_input(field_name="address2", value=contact_data.address_secondary)
        if contact_data.phone_secondary is not None:
            self.app.page_objects.text_input(field_name="phone2", value=contact_data.phone_secondary)
        if contact_data.notes is not None:
            self.app.page_objects.text_input(field_name="notes", value=contact_data.notes)