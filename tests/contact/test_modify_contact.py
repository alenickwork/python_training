# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
"""

from model.contact import Contact
from model.contacts_list import ContactsList
from random import randrange

def test_modify_contact(app):
    if app.contact.count == 0:
        test_contact = Contact()
        test_contact.dummy()
        app.contact.create(test_contact)

    old_contacts = ContactsList(app)

    index = randrange(old_contacts.members_number_hashed)

    test_contact_new = Contact(lastname="random",anniversary_month="random")
    test_contact_new.id = old_contacts.members[index].id

    app.contact.modify_by_index(index, test_contact_new)

    new_contacts = ContactsList(app)

    print("Validate num of elements in list")
    assert old_contacts.members_number_hashed == new_contacts.members_number
    print("Done")


    print("Validate modified element's fields in list")
    old_contacts.members[index] = test_contact_new
    assert old_contacts == new_contacts
    print("Done")
