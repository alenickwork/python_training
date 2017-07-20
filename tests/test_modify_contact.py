# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
"""

from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count == 0:
        test_contact = Contact()
        test_contact.dummy()
        app.contact.create(test_contact)
    test_contact_new = Contact(lastname="random",anniversary_month="random")
    app.contact.modify_first(test_contact_new)
