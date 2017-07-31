# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #4: refactor for fixture usage
"""

from model.group import Group
from model.groups_list import GroupsList

def test_add_group(app):
    old_groups = GroupsList(app)

    group = Group()
    group.dummy()
    app.group.create(group)

    new_groups = GroupsList(app)

    print("Validate +1 element in groups list")
    assert old_groups.members_number_hashed +1 == new_groups.members_number
    print("Done")

    print("Validate new element's field in groups list")
    old_groups.members.append(group)
    assert old_groups == new_groups
    print("Done")

def test_add_empty_group(app):
    old_groups = GroupsList(app)

    empty_group = Group(name = "", header = "", footer = "")
    app.group.create(empty_group)

    new_groups = GroupsList(app)

    print("Validate +1 element in groups list")
    assert old_groups.members_number_hashed +1 == new_groups.members_number
    print("Done")

    print("Validate new element's field in groups list")
    old_groups.members.append(empty_group)
    assert old_groups == new_groups
    print("Done")
