from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact("Andrey", "Andreev", "Andreevich", "AndreyCo", "Chicago, Washington 100-200", "+999999999", "+765443333", "+9993333333", "andreyandreev@andreyco.com"))
    app.session.logout()