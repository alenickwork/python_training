# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #7: modify group
"""

from model.group import Group

def test_modify_group(app):

    app.session.login(username = "admin", password = "secret")
    test_group = Group()
    test_group.dummy()
    app.group.create(test_group)
    test_group_new = Group(name = "random")
    app.group.modify(test_group, test_group_new)
    app.session.logout()
