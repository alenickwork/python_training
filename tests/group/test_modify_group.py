from model.group import Group, clean
import random

def test_modify_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        test_group = Group()
        test_group.dummy()
        app.group.create(test_group)

    old_groups = db.get_group_list()

    group = random.choice(old_groups)

    test_group_new = Group(name = "random")
    test_group_new.id = group.id

    app.group.modify_by_id(group.id, test_group_new)

    new_groups = db.get_group_list()

    assert len(old_groups) == len(new_groups)

    old_groups[old_groups.index(group)] = test_group_new

    assert old_groups == new_groups

    if check_ui:
        assert sorted(map(clean, new_groups), key = Group.id_or_max) == \
            sorted(app.group.get_group_list(), key = Group.id_or_max)
