# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #6: delete group
"""

from model.group import Group

def test_delete_1st_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.delete_first_group()
    app.session.logout()

def test_delete_group(app):
    app.session.login(username = "admin", password = "secret")
    test_group = Group()
    test_group.dummy()
    app.group.create(test_group)
    app.group.delete(test_group)
    app.session.logout()