from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from selenium.webdriver.support.select import Select

class ContactUsPage:

    # Locators
    CONTACTUS = (By.XPATH, "//div[@id='contact-link']//a[contains(text(),'Contact us')]")
    SUBJECT_HEADING = (By.XPATH, "//select[@id='id_contact']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    ORDER_REFERENCE = (By.XPATH, "//select[@name='id_order']")
    MESSAGE = (By.XPATH, "//textarea[@id='message']")
    SEND = (By.XPATH, "//span[contains(text(),'Send')]")
    SUCESS_ALERT = (By.XPATH, "//p[@class='alert alert-success']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Click on SignIn Button in landing page")
    def clickOnContactUsButton(self):
        signup = self.browser.find_element(*self.CONTACTUS)
        signup.click()

    @allure.step("Choose the Subject Heading from dropdown")
    def chooseSubjectHeading(self,subjectHeader):
        subject_heading_Locator = Select(self.browser.find_element(*self.SUBJECT_HEADING))
        subject_heading_Locator.select_by_visible_text(subjectHeader)

    @allure.step("Enter Email Address")
    def enterEmailAddress(self, emailAddress):
        email_Address_loctor = self.browser.find_element(*self.EMAIL)
        email_Address_loctor.click()
        email_Address_loctor.send_keys(emailAddress)

    @allure.step("Enter message for reference")
    def enterMessage(self, messageInfo):
        message_Locator = self.browser.find_element(*self.MESSAGE)
        message_Locator.click()
        message_Locator.send_keys(messageInfo)


    @allure.step("Click on Send Button")
    def clickOnSendButton(self):
        send_Btn_Locator = self.browser.find_element(*self.SEND)
        send_Btn_Locator.click()

    @allure.step("Assert Signout after sucessful user registration")
    def assertSucessAlert(self):
        sucess_alert_locator = self.browser.find_element(*self.SUCESS_ALERT)
        if sucess_alert_locator.is_displayed():
            print('SUCEESS Alert message is found.')
        else:
            print('SUCEESS Alert message is Not found..!!')