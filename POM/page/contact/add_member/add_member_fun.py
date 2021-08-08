import allure
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from POM.page.base_page import BasePage
from POM.page.contact.add_member.from_input.Input_add_member import InputAddMember


class AddMemberFun(BasePage):
    def from_camera(self):
        pass


    def from_input(self):
        self.swipe_find("D:/xueqiu_demo/POM/page/contact/add_member/add_member_fun.yaml")
        # toast_element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@text='添加成功']"))


        return InputAddMember(self.driver)

    def if_toast(self):
        WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element(MobileBy.XPATH,'//*[@text="添加成功"]'))



    def from_phone(self):
        pass
    def from_wechat(self):
        pass