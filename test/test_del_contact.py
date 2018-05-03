from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname = "testname",middlename= "testmiddlename", lastname= "testlastname"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)