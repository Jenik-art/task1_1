from datetime import time

from model.contact import Contact
from model.group import Group
import random

def test_delete_contact_from_group(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname = "testname",middlename= "testmiddlename", lastname= "testlastname"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
        groups = db.get_group_list()
        group = random.choice(groups)
        app.contact.delete_contact_from_grou(group.id)
