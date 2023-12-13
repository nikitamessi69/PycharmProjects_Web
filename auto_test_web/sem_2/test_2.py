import yaml
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


# def test_step1(site, log_xpath, pass_xpath, btn_xpath, result_xpath):
#     input1 = site.find_element("xpath", log_xpath)
#     input1.send_keys("test")
#     input2 = site.find_element("xpath", pass_xpath)
#     input2.send_keys("test")
#     btn = site.find_element("xpath", btn_xpath)
#     btn.click()
#     err_label = site.find_element("xpath", result_xpath)
#     assert err_label.text == "401"


def test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login):
    input1 = site.find_element("xpath", log_xpath)
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", pass_xpath)
    input2.send_keys(testdata["password"])
    btn = site.find_element("xpath", btn_xpath)
    btn.click()
    login = site.find_element("xpath", result_login)
    assert login.text == "Blog"


def test_create_post(site, create_post, title_post, descrip_post, content_post, save_post, title_save, log_xpath,
                     btn_xpath, pass_xpath, result_login):
    test_step2(site, log_xpath, pass_xpath, btn_xpath, result_login)

    btn_create = site.find_element("xpath", create_post)
    btn_create.click()

    time.sleep(2)

    tittle_input = site.find_element("xpath", title_post)
    tittle_input.send_keys("Let Everything")

    description_input = site.find_element("xpath", descrip_post)
    description_input.send_keys("Will be Alright")

    content_input = site.find_element("xpath", content_post)
    content_input.send_keys("All the Time")

    btn_save = site.find_element("xpath", save_post)
    btn_save.click()

    time.sleep(2)

    tittle = site.find_element("xpath", title_save)
    assert tittle.text == "Let Everything"
