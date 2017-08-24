from model.contact import Contact, clean
import random

def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        test_contact = Contact()
        test_contact.dummy()
        app.contact.create(test_contact)

    old_contacts = db.get_contact_list()

    cont = random.choice(old_contacts)

    test_contact_new = Contact(lastname="random",anniversary_month="random")
    test_contact_new.id = cont.id

    app.contact.modify_by_id(cont.id, test_contact_new)

    new_contacts = db.get_contact_list()

    assert len(old_contacts) == len(new_contacts)

    old_contacts[old_contacts.index(cont)] = test_contact_new

    assert old_contacts == new_contacts

    if check_ui:
        assert sorted(map(clean, new_contacts), key = Contact.id_or_max) == \
            sorted(app.contact.get_contacts_list(), key = Contact.id_or_max)


