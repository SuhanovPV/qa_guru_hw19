import os

import allure
import allure_commons
import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
from appium import webdriver
from qa_guru_hw19.utils import allure_attach
import config


def pytest_addoption(parser):
    parser.addoption(
        '--platform',
        default='android'
    )


def set_android_options():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',
        "app": config.app,
        'bstack:options': {
            "sessionName": "BStack first_test",
            "projectName": config.project,
            "userName": config.bstack_username,
            "accessKey": config.bstack_accesskey
        }
    })
    return options


def set_ios_options():
    options = XCUITestOptions().load_capabilities({
        "deviceName": "iPhone 12 Pro Max",
        "platformName": "ios",
        "platformVersion": "16",
        "app": config.app,
        "bstack:options": {
            "sessionName": "BStack first_test",
            "projectName": config.project,
            "userName": config.bstack_username,
            "accessKey": config.bstack_accesskey
        }
    })
    return options


@pytest.fixture(scope='function', autouse=True)
def mobile_settings(request):
    platform = request.config.getoption('--platform')
    if platform == 'android':
        options = set_android_options()
    elif platform == 'ios':
        options = set_ios_options()
    else:
        return

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options,
        )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield platform

    allure_attach.bstack_screenshot(browser)

    allure_attach.bstack_page_source(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    allure_attach.video(session_id)
