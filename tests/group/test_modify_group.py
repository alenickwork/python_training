# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #7: modify group
"""

from model.group import Group
from model.groups_list import GroupsList
from random import randrange

def test_modify_group(app):
    if app.group.count == 0:
        test_group = Group()
        test_group.dummy()
        app.group.create(test_group)

    old_groups = GroupsList(app)


    index = randrange(old_groups.members_number_hashed)

    test_group_new = Group(name = "random")
    test_group_new.id = old_groups.members[index].id

    app.group.modify_by_index(index, test_group_new)

    new_groups = GroupsList(app)

    print("Validate num of elements in groups list")
    assert old_groups.members_number_hashed == new_groups.members_number
    print("Done")

    print("Validate modified element's fields in groups list")
    old_groups.members[index] = test_group_new
    assert old_groups == new_groups
    print("Done")