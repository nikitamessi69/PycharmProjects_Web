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
    testpage.enter_pswd("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 starting")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pswd(testdata["password"])
    testpage.click_login_button()
    assert testpage.get_login_text() == "Blog"


# def test_create_post(browser):
#     test_step2(browser)
#     logging.info("Test create post start")
#     testpage = OperationsHelper(browser, testdata["address"])
#     testpage.go_to_site()
#     testpage.click_create_post_button()
#     time.sleep(testdata["sleep_time"])
#     testpage.enter_title_post("Let Everything")
#     testpage.enter_descrip_post("Will be Alright")
#     testpage.enter_content_post("All the Time")
#     testpage.click_save_post_button()
#     time.sleep(testdata["sleep_time"])
#     assert testpage.title_save() == "Let Everything"


def test_create_post(browser):
    test_step2(browser)
    logging.info("Test create post start")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.go_to_site()
    testpage.click_create_post_button()
    time.sleep(testdata["sleep_time"])
    testpage.enter_title_post("Let Everything")
    testpage.enter_descrip_post("Will be Alright")
    testpage.enter_content_post("All the Time")
    testpage.click_save_post_button()
    time.sleep(testdata["sleep_time"])
    assert testpage.title_save() == "Let Everything"
    testpage.test_contact_us()
