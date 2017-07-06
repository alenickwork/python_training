# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
import os

from model.contact import Contact

def test_delete_contact(app):
    app.session.login(username = "admin",
              password = "secret")
    test_contact = Contact()
    test_contact.dummy()
    app.contact.create(test_contact)
    app.contact.delete(test_contact)
    app.session.logout()
