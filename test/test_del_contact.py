
def test_task_1_3(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()