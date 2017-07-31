# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #4: refactor for fixture usage
"""
import os

from model.contact import Contact
from model.contacts_list import ContactsList

from data import file as photo_link

def test_add_contact(app):
    old_contacts = ContactsList(app)
    cont = Contact(firstname = "test_fn",
                                    middlename = "test_mn",
                                    lastname = "test_ln",
                                    nickname = "test_nn",
                                    photo_link = photo_link,
                                    title = "test_title",
                                    company = "test_c",
                                    address = "test_addr",
                                    home_phone = "test_hph",
                                    mobile_phone = "test_mph",
                                    work_phone = "test_wph",
                                    fax = "test_fx",
                                    email_prior = "test_em1",
                                    email_2 = "test_e2",
                                    email_3 = "test_e3",
                                    homepage = "test_hp",
                                    birthday_day = "15",
                                    birthday_month="March",
                                    birthday_year="1982",
                                    anniversary_day = "30",
                                    anniversary_month="April",
                                    anniversary_year="2011",
                                    address_secondary = "test_addr2",
                                    phone_secondary = "test_ph2",
                                    notes = "12121221")
    app.contact.create(cont)

    new_contacts = ContactsList(app)

    print("Validate +1 element in list")
    assert old_contacts.members_number_hashed + 1 == new_contacts.members_number
    print("Done")

    print("Validate new element's field in list")
    old_contacts.members.append(cont)
    assert old_contacts == new_contacts
    print("Done")
