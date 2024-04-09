import pytest
import yaml
from rest_api import res_post, data_get, res_post_2
from testpage import OperationsHelper

with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    X_Auth_Token = data['token']

with open('datatest.yaml') as f:
    data = yaml.safe_load(f)
    status_error = data['status_error']
    address = data['address']
    username = data['USERNAME']
    password = data['PASSWORD']


def test_1():
    assert X_Auth_Token == res_post.json()['token']


def test_2():
    assert "title" in data_get.text


def test_3():
    assert "testtitle" in res_post_2.text


def test_4(browser):
    test_page = OperationsHelper(browser, address)
    test_page.go_to_site()
    test_page.enter_login('test')
    test_page.enter_pass('test')
    test_page.click_login_button()
    assert test_page.get_error_text() == status_error


def test_5(browser):
    test_page = OperationsHelper(browser, address)
    test_page.go_to_site()
    test_page.enter_login(username)
    test_page.enter_pass(password)
    test_page.click_login_button()
    assert test_page.get_username_label() == f'Hello, GB2023083b37d8'


if __name__ == '__main__':
    pytest.main(['-vv'])
