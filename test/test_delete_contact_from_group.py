from datetime import time
from random import randrange
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_delete_contact_from_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname = "testname",middlename= "testmiddlename", lastname= "testlastname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.open_group_with_contact_page(group.id)
    contacts_in_group = app.contact.get_contact_list_from_group_page()
    if len(app.contact.get_contact_list_from_group_page()) == 0:
        index = 0
        app.contact.add_contact_to_group(index, group.id)
        app.open_home_page()
        app.contact.open_group_with_contact_page(group.id)
        app.contact.delete_contact_from_group(index)
    else:
        index = randrange(len(contacts_in_group))
        app.contact.delete_contact_from_group(index)
    assert app.contact.get_contact_list_from_group_page() in db_orm.get_contacts_not_in_group(group)
