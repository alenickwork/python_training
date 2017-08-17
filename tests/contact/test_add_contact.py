# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #4: refactor for fixture usage
"""
import os

from model.contact import Contact
from model.contacts_list import ContactsList

from data import file as photo_link
import pytest
import random
import string
def generate_str(prefix = "", maxlen = 20):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname = "",
                    middlename = "",
                    lastname = "",
                    nickname = "",
                    title = "",
                    company = "",
                    address = "",
                    home_phone = "",
                    mobile_phone = "",
                    work_phone = "",
                    fax = "",
                    email_prior = "",
                    email_2 = "",
                    email_3 = "",
                    homepage = "",
                    address_secondary = "",
                    phone_secondary = "",
                    notes = "")] + [
    Contact(firstname=generate_str("name",random.randint(5,20)),
            middlename=generate_str("middlename",random.randint(5,20)),
            lastname=generate_str("lastname",random.randint(5,20)),
            nickname=generate_str("nickname",random.randint(5,20)),
            title=generate_str("title",random.randint(5,20)),
            company=generate_str("company",random.randint(5,20)),
            address=generate_str("address",random.randint(5,20)),
            home_phone=generate_str("home_phone",random.randint(5,20)),
            mobile_phone=generate_str("mobile_phone",random.randint(5,20)),
            work_phone=generate_str("work_phone",random.randint(5,20)),
            fax=generate_str("fax",random.randint(5,20)),
            email_prior=generate_str("email_prior",random.randint(5,20)),
            email_2=generate_str("email_2",random.randint(5,20)),
            email_3=generate_str("email_3",random.randint(5,20)),
            homepage=generate_str("homepage",random.randint(5,20)),
            address_secondary=generate_str("address_secondary",random.randint(5,20)),
            phone_secondary=generate_str("phone_secondary",random.randint(5,20)),
            notes=generate_str("notes",random.randint(5,20)))
            for i in range(5)
            ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app,contact):
    old_contacts = ContactsList(app)
    app.contact.create(contact)

    new_contacts = ContactsList(app)

    print("Validate +1 element in list")
    assert old_contacts.members_number_hashed + 1 == new_contacts.members_number
    print("Done")

    print("Validate new element's field in list")
    old_contacts.members.append(contact)
    assert old_contacts == new_contacts
    print("Done")
