import yaml
import time
from TestPage import OperationsHelper
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test1 starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_profile_text() == "Hello, igorkrut777"


def test_create_post(browser):
    test_step2(browser)
    logging.info("Test create post start")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.click_to_do_new_post()
    time.sleep(testdata["sleep_time"])
    testpage.enter_title("Let Everything")
    testpage.enter_description("Will be Alright")
    testpage.enter_content("All the Time")
    testpage.click_save_post_button()
    time.sleep(testdata["sleep_time"])
    assert testpage.get_title_text() == "Let Everything"


def test_contact_us(browser):
    logging.info("Test4 starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.click_contact_button()
    testpage.enter_name("Mr.Bean")
    testpage.enter_email("mrbean@mail.ru")
    testpage.enter_contact_content("contact")
    testpage.contact_us_save_button()
    time.sleep(testdata["sleep_time"])
    assert testpage.get_alert_text() == "Form successfully submitted"
