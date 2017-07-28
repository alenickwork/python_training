# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #6: delete group
"""

from model.group import Group
from model.groups_list import GroupsList

def test_delete_1st_group(app):
    if app.group.count == 0:
        test_group = Group()
        test_group.dummy()
        app.group.create(test_group)
    old_groups = GroupsList(app)

    app.group.delete_first_group()

    new_groups = GroupsList(app)

    print("Validate -1 element in groups list")
    assert old_groups.members_number - 1 == new_groups.members_number
    print("Done")

    print("Validate elements equ in groups list")
    old_groups.members[0:1] = []
    assert old_groups == new_groups
    print("Done")

def test_delete_group(app):
    test_group = Group()
    test_group.dummy()
    app.group.create(test_group)

    old_groups = GroupsList(app)

    app.group.delete(test_group)

    new_groups = GroupsList(app)

    print("Validate -1 element in groups list")
    assert old_groups.members_number - 1 == new_groups.members_number
    print("Done")

    print("Validate elements equ in groups list")
    old_groups.members[-1:] = []
    assert old_groups == new_groups
    print("Done")
