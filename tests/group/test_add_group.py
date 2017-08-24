from model.group import Group, clean
import time

def test_add_group(app, db, json_groups, check_ui):

    group = json_groups

    old_groups = db.get_group_list()

    app.group.create(group)

    new_groups = db.get_group_list()

    old_groups.append(group)

    start = time.time()
    while True:
        try:
            assert old_groups == new_groups
            break
        except AssertionError:
            assert time.time()-start < 30, "Timeout! Groups lists are different"

    if check_ui:
        assert sorted(map(clean, new_groups), key = Group.id_or_max) == \
            sorted(app.group.get_group_list(), key = Group.id_or_max)

