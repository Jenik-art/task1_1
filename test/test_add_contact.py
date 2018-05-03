# -*- coding: utf-8 -*-
from fixture.contact import contactHelper
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.add(Contact("Ivan", "Ivanovich", "Ivanov", "IvanCo", "New York, Brighton beach 100-200", "+1111111111", "+12222222", "+3333333", "ivanovivan@ivanco.com"))
    new_contacts = app.contact.get_contact_list
    assert len(old_contacts) +1 == len(new_contacts)
