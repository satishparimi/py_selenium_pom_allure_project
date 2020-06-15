from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure


class HomePage:
    # Locators
    SIGN_UP = (By.XPATH, "//a[@class='login']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    @allure.step("click on SignIn Button in landing page")
    def clickOnSignInBuggon(self):
        signup = self.browser.find_element(*self.SIGN_UP)
        signup.click()
