# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #6: delete group
"""

from model.group import Group
from model.groups_list import GroupsList
from random import randrange

def test_delete_some_group(app):
    if app.group.count == 0:
        test_group = Group()
        test_group.dummy()
        app.group.create(test_group)
    old_groups = GroupsList(app)

    index = randrange(old_groups.members_number_hashed)
    app.group.delete_by_index(index)

    new_groups = GroupsList(app)

    print("Validate -1 element in groups list")
    assert old_groups.members_number_hashed - 1 == new_groups.members_number
    print("Done")

    print("Validate elements equ in groups list")
    del old_groups.members[index]
    assert old_groups == new_groups
    print("Done")

def test_delete_group(app):
    test_group = Group()
    test_group.dummy()
    app.group.create(test_group)

    old_groups = GroupsList(app)
    test_group.id = old_groups.normalized[-1].id

    app.group.delete(test_group)

    new_groups = GroupsList(app)

    print("Validate -1 element in groups list")
    assert old_groups.members_number_hashed - 1 == new_groups.members_number
    print("Done")

    print("Validate elements equ in groups list")
    old_groups.delete_by_id(test_group.id)
    assert old_groups == new_groups
    print("Done")
