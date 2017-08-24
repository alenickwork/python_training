from model.contacts_list import ContactsList

def test_add_contact(app,json_contacts):
    contact = json_contacts
    old_contacts = ContactsList(app)
    app.contact.create(contact)

    new_contacts = ContactsList(app)

    print("Validate +1 element in list")
    assert old_contacts.members_number_hashed + 1 == new_contacts.members_number
    print("Done")

    print("Validate new element's field in list")
    old_contacts.members.append(contact)
    assert old_contacts == new_contacts
    print("Done")
