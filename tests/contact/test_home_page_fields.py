import pytest
import re

class TestHomePageContact:
    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, app):
        self.app = app
        self.contact_from_home_page = self.app.contact.get_contacts_list()[0]
        self.contact_from_edit_page = self.app.contact.get_contact_info_from_edit_page(0)

    def test_lastname(self):
        assert self.contact_from_home_page.lastname == self.contact_from_edit_page.lastname

    def test_firstname(self):
        assert self.contact_from_home_page.firstname == self.contact_from_edit_page.firstname

    def test_mail(self):
        assert self.contact_from_home_page.all_mails_from_homepage == \
               merge_mails_like_on_home_page(self.contact_from_edit_page)

    def test_phones(self):
        assert self.contact_from_home_page.all_phones_from_homepage == \
               merge_phones_like_on_home_page(self.contact_from_edit_page)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda _: _ != "",
                            map(lambda _: clear(_),
                                filter(lambda _: _ is not None,
                                       [contact.home_phone,
                                          contact.mobile_phone,
                                          contact.work_phone,
                                          contact.phone_secondary]))))

def merge_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda _: _ != "",
                            map(lambda _: clear(_),
                                filter(lambda _: _ is not None,
                                       [contact.email_prior,
                                          contact.email_2,
                                          contact.email_3]))))
def clear(s):
    return re.sub('[() -]', '', s)
