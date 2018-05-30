import re

from selenium.webdriver.support.select import Select

from model.contact import Contact
import time
from model.group import Group
import random
from random import randrange

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

    def click_edit_by_id(self,id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()

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

    def edit_contact_by_id(self,id,contact):
        wd = self.app.wd
        self.click_edit_by_id(id)
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
                f_name = cells[2].text
                l_name = cells[1].text
                address= cells[3].text
                all_emails=cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                all_phones= cells[5].text
                self.contact_cache.append(Contact(lastname=l_name,firstname = f_name, id=id, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self,index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(lastname=lastname,firstname = firstname, id=id, address=address,email=email, email2=email2, email3=email3, homephone=homephone,workphone=workphone,
                       mobilephone=mobilephone, secondaryphone= secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        memberof = re.search("Member of: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone, memberof=memberof)

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name("entry")[index]
        cell = element.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self,index):
        wd = self.app.wd
        self.app.open_home_page()
        element = wd.find_elements_by_name("entry")[index]
        cell = element.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.choose_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        time.sleep(1)
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home").click()
        self.contact_cache = None

    def choose_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def add_contact_to_group(self,index,id):
        wd = self.app.wd
        self.app.open_home_page()
        self.choose_contact_by_index(index)
        self.choose_group_for_contact(id)
        wd.find_element_by_name("add").click()

    def choose_group_for_contact(self,id):
        wd = self.app.wd
        select = Select(wd.find_element_by_css_selector("select[name='to_group']"))
        select.select_by_value('%s' % id)

    def choose_group_with_contact(self, id):
        wd = self.app.wd
        select = Select(wd.find_element_by_css_selector("select[name='group']"))
        select.select_by_value('%s' % id)
        contacts_in_group = self.get_contact_list()
        if contacts_in_group == []:
            index = randrange(len(contacts_in_group))
            self.add_contact_to_group(index,id)


    def delete_contact_from_group(self, index):
        wd = self.app.wd
        self.choose_contact_by_index(index)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text("home").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_group_with_contact_page(self,id):
        wd = self.app.wd
        select = Select(wd.find_element_by_css_selector("select[name='group']"))
        select.select_by_value('%s' % id)

    def get_contact_list_from_group_page(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache =[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                f_name = cells[2].text
                l_name = cells[1].text
                address= cells[3].text
                all_emails=cells[4].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("id")
                all_phones= cells[5].text
                self.contact_cache.append(Contact(lastname=l_name,firstname = f_name, id=id, address=address,
                                                  all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)