import allure
from appium.webdriver.common.mobileby import MobileBy

from POM.page.base_page import BasePage
from POM.page.contact.add_member.add_member_fun import AddMemberFun


class ContactPage(BasePage):
    def add_customer(self):     #有下一路径的写在最上面
        pass


    def add_member(self):
        self.step("D:/xueqiu_demo/POM/page/contact/contact_page.yaml")
        return AddMemberFun(self.driver)

    def view_member(self):
        pass

    def search_contacts(self):
        pass


    def manager_contacts(self):
        pass