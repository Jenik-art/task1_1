# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_task_1_1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="task_1_1", header="Header", footer="Footer"))
    app.session.logout()

