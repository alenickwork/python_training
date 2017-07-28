# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
"""

from model.contact import Contact
from model.contacts_list import ContactsList

def test_modify_contact(app):
    if app.contact.count == 0:
        test_contact = Contact()
        test_contact.dummy()
        app.contact.create(test_contact)

    old_contacts = ContactsList(app)

    test_contact_new = Contact(lastname="random",anniversary_month="random")
    test_contact_new.id = old_contacts.members[0].id

    app.contact.modify_first(test_contact_new)

    new_contacts = ContactsList(app)

    print("Validate num of elements in list")
    assert old_contacts.members_number == new_contacts.members_number
    print("Done")

    print("Validate modified element's fields in list")
    old_contacts.members[0] = test_contact_new
    assert old_contacts == new_contacts
    print("Done")
