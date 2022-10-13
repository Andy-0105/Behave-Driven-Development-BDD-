import pytest
import calculate
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By

Calculator_web = 'http://localhost/test'

scenarios('./test.feature')

@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()

@given('the Calculator_web page is displayed')
def ddg_home(browser):
    browser.get(Calculator_web)

@given(parsers.parse('I enter {expression}'))
def step_impl(browser, expression):
    input=browser.find_element(By.ID,'input_str')
    input.send_keys(expression)

@when(parsers.parse('I press "=" button'))
def search_phrase(browser):
    browser.find_element(By.ID,'input_button').click()
# Then Steps
@then(parsers.parse('I get the answer {answer}'))
def results_have_one(browser, answer):
   reslt=browser.find_element(By.ID,'output_str').get_attribute("value")
   assert reslt == answer


@then(parsers.parse('I get the same answer {expression2}'))
def results_have_one(browser, expression2):
   reslt=browser.find_element(By.ID,'output_str').get_attribute("value")
   assert int(reslt) == calculate.calculater(expression2)
