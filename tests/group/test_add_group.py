# -*- coding: utf-8 -*-
__author__ = "Elena Dimchenko"
"""
Task #4: refactor for fixture usage
"""

from model.group import Group
from model.groups_list import GroupsList
import pytest

import random
import string
def generate_str(prefix = "", maxlen = 20):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix+''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# testdata = [Group(name = name, header = header, footer = footer)
#             for name in ["", generate_str("name",10)]
#             for header in ["", generate_str("header",20)]
#             for footer in ["", generate_str("footer", 20)]
#             ]

testdata = [Group(name = "", header = "", footer = "")] + [
           Group(name = generate_str("name",10),
                  header = generate_str("header",20),
                  footer = generate_str("footer", 20))
            for i in range(5)
            ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = GroupsList(app)
    app.group.create(group)
    new_groups = GroupsList(app)

    print("Validate +1 element in groups list")
    assert old_groups.members_number_hashed +1 == new_groups.members_number
    print("Done")

    print("Validate new element's field in groups list")
    old_groups.members.append(group)
    assert old_groups == new_groups
    print("Done")
