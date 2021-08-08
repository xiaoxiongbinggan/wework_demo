import yaml
from appium.webdriver import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver=driver


    def find(self,by,locator):
        return self.driver.find_element(by,locator)

    def swipe_find(self,path):
        for i in range(0,10):
            if i == 9:
                raise NoSuchElementException("找了3次没找到")
            try:
                self.step(path)
            except :
                print("未找到，进行滑动")
                size=self.driver.get_window_size()
                startx=size["width"]/2
                endx=startx
                starty=size["height"]*0.8
                endy=size["height"]*0.3
                duration = 2000  # 2s
                self.driver.swipe(startx,starty,endx,endy,duration)

    def step(self,path):
        with open(path,encoding="utf-8") as f:
            steps:list[dict]=yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element=self.find(step["by"],step["locator"])
                    if "action" in step.keys():
                        if step["action"]=="click":
                            element.click()
                        if step["action"]=="sendkeys":
                            element.send_keys(step["value"])





