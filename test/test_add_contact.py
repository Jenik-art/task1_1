# -*- coding: utf-8 -*-

from model.contact import Contact





def test_task_1_3(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact("Ivan", "Ivanovich", "Ivanov", "IvanCo", "New York, Brighton beach 100-200", "+1111111111", "+12222222", "+3333333", "ivanovivan@ivanco.com"))
    app.session.logout()
