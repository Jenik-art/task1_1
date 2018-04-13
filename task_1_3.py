# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_task_1_3(app):
    app.login(username="admin", password="secret")
    app.init_add_contact(Contact( "Ivan", "Ivanovich", "Ivanov", "IvanCo", "New York, Brighton beach 100-200","+1111111111", "+12222222", "+3333333", "ivanovivan@ivanco.com"))
    app.logout()
