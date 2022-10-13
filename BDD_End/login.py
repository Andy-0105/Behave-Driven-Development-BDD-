
import pytest
from pytest_bdd import scenarios,given,when,then,parsers
from selenium import webdriver
from selenium.webdriver.common.by import By

web_url='http://127.0.0.1:2200'
scenarios('./login.feature')
@pytest.fixture
def browser():
    web=webdriver.Chrome()
    web.implicitly_wait(10)
    yield web
    web.quit()
@given('I navigate to login page')
def calc_web(browser):
    browser.get(web_url)
@given(parsers.parse('I enter vaild {user_id} and {password}'))
def vaild(browser,user_id,password):
    browser.user_id=user_id
    browser.password=password
    browser.user_id_input=browser.find_element(By.ID,'user_id')
    browser.user_id_input.send_keys(user_id)
    browser.password_input=browser.find_element(By.ID,'password')
    browser.password_input.send_keys(password)
@when('I click on submit button')
def click(browser):
    browser.find_element(By.ID,'submit').click()
@then(parsers.parse('I login in successful'))
def successful(browser):
    if browser.user_id =='123' and browser.password =='123':
        assert browser.find_element(By.ID,'result').text == 'login successfully'
    else:
        assert browser.find_element(By.ID,'result').text == 'login failed'