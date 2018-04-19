# -*- coding: utf-8 -*-

from model.group import Group


def test_task_1_1(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="task_1_1", header="Header", footer="Footer"))
    app.session.logout()

