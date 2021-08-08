import allure
import pytest


@allure.feature("1")
def test_1():
    print(1)

@allure.story("2")
def test_2():
    print(2)

@allure.step("3")
def test_3():
    print(3)

if __name__ == '__main__':
    pytest.main(test_1(),test_2())


