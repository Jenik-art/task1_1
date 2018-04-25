from model.contact import Contact

def test_del_first_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(firstname = "testname",middlename= "testmiddlename", lastname= "testlastname"))
    app.contact.delete_first_contact()
