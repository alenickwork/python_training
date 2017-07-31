# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
import os

from model.contact import Contact
from model.contacts_list import ContactsList
from random import randrange

def test_delete_some_contact(app):
    if app.contact.count == 0:
        test_contact = Contact()
        test_contact.dummy()
        app.contact.create(test_contact)
    old_contacts = ContactsList(app)

    index = randrange(old_contacts.members_number_hashed)
    app.contact.delete_by_index(index)

    new_contacts = ContactsList(app)

    print("Validate -1 element in list")
    assert old_contacts.members_number_hashed - 1 == new_contacts.members_number
    print("Done")

    print("Validate elements equ in contacts list")
    del old_contacts.members[index]
    assert old_contacts == new_contacts
    print("Done")


def test_delete_contact(app):
    test_contact = Contact()
    test_contact.dummy()
    app.contact.create(test_contact)

    old_contacts = ContactsList(app)
    test_contact.id = old_contacts.normalized[-1].id

    app.contact.delete(test_contact)
    new_contacts = ContactsList(app)

    print("Validate -1 element in list")
    assert old_contacts.members_number_hashed - 1 == new_contacts.members_number
    print("Done")

    print("Validate elements equ in contacts list")
    old_contacts.delete_by_id(test_contact.id)
    assert old_contacts == new_contacts
    print("Done")
