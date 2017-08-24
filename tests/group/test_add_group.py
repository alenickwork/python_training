from model.groups_list import GroupsList

def test_add_group(app, json_groups):
    group = json_groups
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
