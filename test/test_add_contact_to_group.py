from model.contact import Contact
from model.group import Group
from random import randrange
from fixture.orm import ORMFixture
import random

db_orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname = "testname",middlename= "testmiddlename", lastname= "testlastname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    len_contact_from_home_page = app.contact.get_contact_list()
    index = randrange(len(len_contact_from_home_page))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(app.contact.get_contact_list_from_group_page()) == len(db.get_contact_list()) or app.contact.get_contact_list()[index] in db_orm.get_contacts_in_group(group) :
        app.contact.open_group_with_contact_page(group.id)
        app.contact.delete_contact_from_group(index)
    else:
        contact = app.contact.add_contact_to_group(index,group.id)
    assert app.contact.get_contact_list()[index] in db_orm.get_contacts_in_group(group)


