import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_text_input(mobile_settings):
    if mobile_settings == 'android':
        pytest.skip('test for ios, not for android')
    with allure.step('Input text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys('Pumpkin Eater\n')
    with allure.step('Find sended text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text('Pumpkin Eater'))
