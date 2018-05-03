from model.contact import Contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname = "testname",middlename= "testmiddlename", lastname= "testlastname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname = "Andrey", lastname ="Andreev", middlename = "Andreevich"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
