# -*- coding: utf-8 -*-

from model.group import Group


def test_task_1_1(app):
    app.group.create(Group(name="task_1_1", header="Header", footer="Footer"))


