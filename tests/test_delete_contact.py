# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
import os

from model.contact import Contact
from model.contacts_list import ContactsList

def test_delete_first_contact(app):
    if app.contact.count == 0:
        test_contact = Contact()
        test_contact.dummy()
        app.contact.create(test_contact)
    old_contacts = ContactsList(app)

    app.contact.delete_first()
    new_contacts = ContactsList(app)

    print("Validate -1 element in list")
    assert old_contacts.members_number - 1 == new_contacts.members_number
    print("Done")

    print("Validate elements equ in contacts list")
    old_contacts.members[0:1] = []
    assert old_contacts == new_contacts
    print("Done")


def test_delete_contact(app):
    test_contact = Contact()
    test_contact.dummy()
    app.contact.create(test_contact)

    old_contacts = ContactsList(app)

    app.contact.delete(test_contact)
    new_contacts = ContactsList(app)

    print("Validate -1 element in list")
    assert old_contacts.members_number - 1 == new_contacts.members_number
    print("Done")

    print("Validate elements equ in contacts list")
    old_contacts.members[-1:] = []
    assert old_contacts == new_contacts
    print("Done")
