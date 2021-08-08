import allure
import pytest

from POM.page.app import App


class TestAddMember():
    def setup(self):
        self.app = App()
    # @pytest.mark.parametrize
    @allure.story("添加成员")
    def test_member(self):
        with allure.step("输入信息"):
            self.app.start().goto_contact().add_member().from_input().input_add_member().if_toast()



if __name__ == '__main__':
    pytest.main()