from model.contact import Contact, clean

def test_add_contact(app,json_contacts, db, check_ui):

    contact = json_contacts

    old_contacts = db.get_contact_list()

    app.contact.create(contact)

    new_contacts = db.get_contact_list()

    assert len(old_contacts) + 1 == len(new_contacts)

    old_contacts.append(contact)

    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(map(clean, new_contacts), key = Contact.id_or_max) == \
            sorted(app.contact.get_contacts_list(), key = Contact.id_or_max)
