from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import groupHelper
from fixture.contact import contactHelper
import pytest

class Application:

    def __init__(self,browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)

        self.session = SessionHelper(self)
        self.group = groupHelper(self)
        self.contact = contactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        self.wd.implicitly_wait(2)
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("searchform"))) > 0:
            wd.get(self.base_url)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()