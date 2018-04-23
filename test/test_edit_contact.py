from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname = "Andrey", lastname ="Andreev", middlename = "Andreevich"))
    app.session.logout()