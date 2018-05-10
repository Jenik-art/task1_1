
from model.contact import Contact
class contactHelper:

    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname",contact.firstname)
        self.change_field_value("middlename",contact.middlename)
        self.change_field_value("lastname",contact.lastname)
        self.change_field_value("company",contact.company)
        self.change_field_value("address",contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("email", contact.email)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.choose_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def choose_contact_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def click_edit_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self,index,contact):
        wd = self.app.wd
        self.click_edit_by_index(index)
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        wd.find_element_by_link_text("home").click()
        self.app.open_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
            wd.find_element_by_name(field_name).click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache =[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                l_name = cells[1].text
                f_name = cells[2].text
                #l_name = element.find_element_by_xpath(".//td[2]").text
                #f_name = element.find_element_by_xpath(".//td[3]").text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                all_phones= cells[5].text.splitlines()
                self.contact_cache.append(Contact(lastname=l_name,firstname = f_name, id=id, homephone=all_phones[0],
                                                  mobilephone=all_phones[1],workphone=all_phones[2],secondaryphone=all_phones[3]))
        return list(self.contact_cache)

    def contact_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_elements_by_name("firstname").get_attribute("value")
        lastname = wd.find_elements_by_name("lastname").get_attribute("value")
        id = wd.find_elements_by_name("id").get_attribute("value")
        homephone = wd.find_elements_by_name("home").get_attribute("value")
        workphone = wd.find_elements_by_name("work").get_attribute("value")
        mobilephone = wd.find_elements_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_elements_by_name("phone2").get_attribute("value")
        return Contact(firstname = firstname, lastname=lastname, id= id, homephone=homephone,workphone=workphone,
                       mobilephone=mobilephone, secondaryphone= secondaryphone)


    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name("entry")[index]
        cell = wd.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name("entry")[index]
        cell = wd.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()