from model.group import Group, clean
import random

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        test_group = Group()
        test_group.dummy()
        app.group.create(test_group)
    old_groups = db.get_group_list()

    group = random.choice(old_groups)

    app.group.delete_by_id(group.id)

    new_groups = db.get_group_list()

    assert len(old_groups) - 1 == len(new_groups)

    old_groups.remove(group)

    assert old_groups == new_groups

    if check_ui:
        assert sorted(map(clean, new_groups), key = Group.id_or_max) == \
            sorted(app.group.get_group_list(), key = Group.id_or_max)
