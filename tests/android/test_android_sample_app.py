import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_wiki_search_browser_stack(mobile_settings):
    if mobile_settings == 'ios':
        pytest.skip('test for android, not for ios')
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')

    with allure.step('Verify found content'):
        search_results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        search_results.should(have.size_greater_than(0))
        search_results.first.should(have.text('BrowserStack'))

    with allure.step('Open first founded page'):
        search_results.first.click()


def test_wiki_search_test_ng(mobile_settings):
    if mobile_settings == 'ios':
        pytest.skip('test for android, not for ios')
    with allure.step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('TestNG')
    with allure.step('Verify found content'):
        search_results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        search_results.first.should(have.text("TestNG"))
    with allure.step('Open first founded page'):
        search_results.first.click()
