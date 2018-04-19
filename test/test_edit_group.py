from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="Edited_task_1_1", header="Edited_Header", footer="Edited_Footer"))
    app.session.logout()