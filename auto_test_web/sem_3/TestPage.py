from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    LOCATOR_PSWD_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')

    LOCATOR_RESULT_LOGIN = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    LOCATOR_CREATE_POST = (By.XPATH, '//*[@id="create-btn"]')
    LOCATOR_TITLE_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[1]/div/label/input')
    LOCATOR_DESCRIP_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea')
    LOCATOR_CONTENT_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea')
    LOCATOR_SAVE_POST = (By.XPATH, '//*[@id="create-item"]/div/div/div[7]/div/button/span')
    LOCATOR_TITLE_SAVE = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')

    LOCATOR_CONTACT_BTN = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[2]/a')
    LOCATOR_NAME = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    LOCATOR_EMAIL = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    LOCATOR_CONTENT = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    LOCATOR_SEND_BTN = (By.XPATH, '//*[@id="contact"]/div[4]/button/span')


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pswd(self, word):
        logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_PSWD_FIELD[1]}')
        pswd_field = self.find_element(TestSearchLocators.LOCATOR_PSWD_FIELD)
        pswd_field.clear()
        pswd_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click logging button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_login_text(self):
        login_text = self.find_element(TestSearchLocators.LOCATOR_RESULT_LOGIN, time=2)
        text = login_text.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_RESULT_LOGIN[1]}')
        return text

    def click_create_post_button(self):
        logging.info('Click create post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST).click()

    def enter_title_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_TITLE_POST[1]}')
        title_post = self.find_element(TestSearchLocators.LOCATOR_TITLE_POST)
        title_post.clear()
        title_post.send_keys(word)

    def enter_descrip_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_DESCRIP_POST[1]}')
        descrip_post = self.find_element(TestSearchLocators.LOCATOR_DESCRIP_POST)
        descrip_post.clear()
        descrip_post.send_keys(word)

    def enter_content_post(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_POST[1]}')
        content_post = self.find_element(TestSearchLocators.LOCATOR_CONTENT_POST)
        content_post.clear()
        content_post.send_keys(word)

    def click_save_post_button(self):
        logging.info('Click save post button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST).click()

    # def title_save(self, word):
    #     logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_TITLE_SAVE[1]}')
    #     title_save = self.find_element(TestSearchLocators.LOCATOR_TITLE_SAVE)
    #     title_save.clear()
    #     title_save.send_keys(word)

    def title_save(self):
        title_save = self.find_element(TestSearchLocators.LOCATOR_TITLE_SAVE, time=2)
        text = title_save.text
        logging.info(f'We find text {text} in title save field {TestSearchLocators.LOCATOR_TITLE_SAVE[1]}')
        return text

    def test_contact_us(self):
        logging.info("Test contact us start")
        self.go_to_site()
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_BTN).click()
        self.find_element(TestSearchLocators.LOCATOR_NAME).send_keys("Mister Bean")
        self.find_element(TestSearchLocators.LOCATOR_EMAIL).send_keys("mrbean@bbc.com")
        self.find_element(TestSearchLocators.LOCATOR_CONTENT).send_keys("This is a test message")
        self.find_element(TestSearchLocators.LOCATOR_SEND_BTN).click()
        alert = self.switch_to_alert()
        logging.info(f"We find text {alert.text} in alert")
        assert alert.text == "Form successfully submitted"







    







