from model.contact import Contact
from .helpers.base_list import BaseList

class ContactsList(BaseList):
    def __init__(self,app):
        super(ContactsList, self).__init__(app)
        self.members = self.app.contact.get_contacts_list()
        self.key = Contact.id_or_max
        self.normalize()
    def __eq__(self, other):
        return self.normalized == self.normalized

    @property
    def members_number(self):
        return self.app.contact.count
