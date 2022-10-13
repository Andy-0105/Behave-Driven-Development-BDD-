"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Constants

Google_HOME = 'http://www.google.com'


# Scenarios

scenarios('../web.feature')


# Fixtures

@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


# Given Steps

@given('the Google home page is displayed')
def ddg_home(browser):
    browser.get(Google_HOME)


# When Steps

@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(browser, phrase):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(phrase + Keys.RETURN)


@when(parsers.parse('the user searches for the phrase:\n"""{text}"""'))
def search_long_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)


# Then Steps
@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    xpath = "//div[@id='search']//*[contains(text(), '%s')]" % phrase
	#EC.visibility_of_element_located(By.XPATH, RESULTS_LOCATOR)
	#results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('search')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase