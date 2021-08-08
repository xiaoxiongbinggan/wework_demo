import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from POM.page.base_page import BasePage


class InputAddMember(BasePage):


    def input_add_member(self):
        self.step("D:/xueqiu_demo/POM/page/contact/add_member/from_input/input_add_member.yaml")
        from POM.page.contact.add_member.add_member_fun import AddMemberFun

        return AddMemberFun(self.driver)