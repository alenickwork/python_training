# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #7: modify group
"""

from model.group import Group

def test_modify_group(app):
    if app.group.count == 0:
        test_group = Group()
        test_group.dummy()
        app.group.create(test_group)
    test_group_new = Group(name = "random")
    app.group.modify_first(test_group_new)