class ContactHelper:
    def __init__(self,app):
        self.app = app

    def create(self, contact_data):
        print("Create new contact")
        self._click_new()
        self._enter_data(contact_data)
        self.app.page_objects.submit()

    def _click_new(self):
        print("Go to add new")
        self.app.page_objects.link_click("add new")

    def _enter_data(self, contact_data):
        print("Input contact data")
        self.app.page_objects.text_input(field_name="firstname", value=contact_data.firstname)
        self.app.page_objects.text_input(field_name="middlename", value=contact_data.middlename)
        self.app.page_objects.text_input(field_name="lastname", value=contact_data.lastname)
        self.app.page_objects.text_input(field_name="nickname", value=contact_data.nickname)
        self.app.page_objects.file_select(field_name="photo", value=contact_data.photo_link)
        self.app.page_objects.text_input(field_name="title", value=contact_data.title)
        self.app.page_objects.text_input(field_name="company", value=contact_data.company)
        self.app.page_objects.text_input(field_name="address", value=contact_data.address)
        self.app.page_objects.text_input(field_name="home", value=contact_data.home_phone)
        self.app.page_objects.text_input(field_name="mobile", value=contact_data.mobile_phone)
        self.app.page_objects.text_input(field_name="work", value=contact_data.work_phone)
        self.app.page_objects.text_input(field_name="fax", value=contact_data.fax)
        self.app.page_objects.text_input(field_name="email", value=contact_data.email_prior)
        self.app.page_objects.text_input(field_name="email2", value=contact_data.email_2)
        self.app.page_objects.text_input(field_name="email3", value=contact_data.email_3)
        self.app.page_objects.text_input(field_name="homepage", value=contact_data.homepage)
        self.app.page_objects.dropdown_select(field_name="bday", value=contact_data.birthday_day)
        self.app.page_objects.dropdown_select(field_name="bmonth", value=contact_data.birthday_month)
        self.app.page_objects.text_input(field_name="byear", value=contact_data.birthday_year)
        self.app.page_objects.dropdown_select(field_name="aday", value=contact_data.anniversary_day)
        self.app.page_objects.dropdown_select(field_name="amonth", value=contact_data.anniversary_month)
        self.app.page_objects.text_input(field_name="ayear", value=contact_data.anniversary_year)
        self.app.page_objects.text_input(field_name="address2", value=contact_data.address_secondary)
        self.app.page_objects.text_input(field_name="phone2", value=contact_data.phone_secondary)
        self.app.page_objects.text_input(field_name="notes", value=contact_data.notes)