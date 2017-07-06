# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
"""

from model.contact import Contact

def test_modify_contact(app):

    app.session.login(username = "admin", password = "secret")
    test_contact = Contact()
    test_contact.dummy()
    app.contact.create(test_contact)
    test_contact_new = Contact(lastname="random",anniversary_month="random")
    app.contact.modify(test_contact, test_contact_new)
    app.session.logout()
