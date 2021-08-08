import json

import allure
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from POM.page.base_page import BasePage
from POM.page.contact.contact_page import ContactPage

class App(BasePage):


    def start(self):
        if self.driver==None:
            caps = json.load(open("D:/xueqiu_demo/wework_caps.json", "r", encoding="utf-8"))
            self.driver=webdriver.Remote("http://localhost:4723/wd/hub",caps)
            self.driver.implicitly_wait(10)
        else:
            self.restart()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def goto_msg(self):
        pass


    def goto_contact(self):
        self.step("D:/xueqiu_demo/POM/page/app.yaml")
        return ContactPage(self.driver)

    def goto_platform(self):
        pass
    def goto_mine(self):
        pass