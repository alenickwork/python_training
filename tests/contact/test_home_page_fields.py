import pytest
import re

from model.contact import clean

class TestHomePageContact:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, app, orm):
        self.app = app
        self.orm = orm
        self.contact_from_home_page = self.app.contact.get_contacts_list()
        self.contacts_from_db = self.orm.get_contact_list()
        assert len(self.contact_from_home_page) == len(self.contacts_from_db)

    def test_lastname(self):
        for contact in self.contact_from_home_page:
            assert contact.lastname == clean(self.orm.get_contact_by_id(contact.id)).lastname

    def test_firstname(self):
        for contact in self.contact_from_home_page:
            assert contact.firstname == clean(self.orm.get_contact_by_id(contact.id)).firstname

    def test_mail(self):
        for contact in self.contact_from_home_page:
            assert contact.all_mails_from_homepage == merge_mails_like_on_home_page(self.orm.get_contact_by_id(contact.id, full = True))


    def test_phones(self):
        for contact in self.contact_from_home_page:
            assert contact.all_phones_from_homepage == merge_phones_like_on_home_page(self.orm.get_contact_by_id(contact.id, full = True))


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
