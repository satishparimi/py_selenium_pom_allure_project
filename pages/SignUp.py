from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
from selenium.webdriver.support.select import Select


class SignUpPage:
    # Locators

    ENTER_EMAIL = (By.XPATH, "//input[@id='email_create']")
    GENDER = (By.XPATH, "//input[@id='id_gender1']")
    FIRST_NAME = (By.XPATH, "//input[@id='customer_firstname']")
    LAST_NAME = (By.XPATH, "//input[@id='customer_lastname']")
    PASSWORD = (By.ID, "passwd")
    STREET_ADDRESS = (By.XPATH, "//input[@id='address1']")
    CITY = (By.XPATH, "//input[@id='city']")
    STATE_DropDown = (By.XPATH, "//select[@id='id_state']")
    ZIPCODE = (By.XPATH, "//input[@id='postcode']")
    COUNTRY = (By.XPATH, "//select[@id='id_country']")
    ADDITIONAL_INFO = (By.XPATH, "//textarea[@id='other']")
    MOBILE = (By.XPATH, "//input[@id='phone_mobile']")
    ADDRESS_ALIAS = (By.XPATH, "//input[@id='alias']")
    REGISNTER = (By.XPATH, "//span[contains(text(),'Register')]")
    SIGNOUT = (By.XPATH, "//a[@class='logout']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    @allure.step("enter email ID")
    def enterEmailID(self, email):
        search_input = self.browser.find_element(*self.ENTER_EMAIL)
        search_input.send_keys(email + Keys.RETURN)

    @allure.step("select the gender")
    def selectGender(self):
        genderSelect = self.browser.find_element(*self.GENDER)
        genderSelect.click()

    @allure.step("Enter First Name")
    def enterFirstName(self, firstName):
        first_Name = self.browser.find_element(*self.FIRST_NAME)
        first_Name.send_keys(firstName)

    @allure.step("Enter Last Name")
    def enterLastName(self, lastName):
        last_Name = self.browser.find_element(*self.LAST_NAME)
        last_Name.send_keys(lastName)

    @allure.step("Enter password")
    def enterPassword(self, pwd):
        password = self.browser.find_element(*self.PASSWORD)
        password.click()
        password.send_keys(pwd)

    @allure.step("Enter Contact Address")
    def enterAddress(self, contactAddress):
        address_locator = self.browser.find_element(*self.STREET_ADDRESS)
        address_locator.click()
        address_locator.send_keys(contactAddress)

    @allure.step("Enter City Name")
    def enterCityName(self, cityName):
        city_locator = self.browser.find_element(*self.CITY)
        city_locator.click()
        city_locator.send_keys(cityName)

    @allure.step("Select the state ")
    def selectState(self, stateName):
        state_Dropdown_Locator = Select(self.browser.find_element(*self.STATE_DropDown))
        state_Dropdown_Locator.select_by_visible_text(stateName)

    @allure.step("Enter the zipcode")
    def enterZipcode(self, zipcodeNum):
        zipcode_locator = self.browser.find_element(*self.ZIPCODE)
        zipcode_locator.click()
        zipcode_locator.send_keys(zipcodeNum)

    @allure.step("Select Country")
    def selectCountry(self, countryName):
        country_Dropdown_Locator = Select(self.browser.find_element(*self.COUNTRY))
        country_Dropdown_Locator.select_by_visible_text(countryName)

    @allure.step("Enter the additioal Information")
    def enterAdditionalInfo(self, additionalInformation):
        addtional_info_locator = self.browser.find_element(*self.ADDITIONAL_INFO)
        addtional_info_locator.click()
        addtional_info_locator.send_keys(additionalInformation)

    @allure.step("Enter the Mobile Number")
    def enterMobile(self, mobileNumber):
        mobine_phone_locator = self.browser.find_element(*self.MOBILE)
        mobine_phone_locator.click()
        mobine_phone_locator.send_keys(mobileNumber)

    @allure.step("Enter Alias Name for your Address")
    def address_Alias(self, addressAliasName):
        address_alias_locator = self.browser.find_element(*self.ADDRESS_ALIAS)
        address_alias_locator.click()
        address_alias_locator.send_keys(addressAliasName)

    @allure.step("Click on Register Button")
    def clickOnRegister(self):
        register_Btn_locator = self.browser.find_element(*self.REGISNTER)
        register_Btn_locator.click()

    @allure.step("Assert Signout after sucessful user registration")
    def assertSignOutAfterRegistration(self):
        sign_out_Btn_locator = self.browser.find_element(*self.SIGNOUT)
        if sign_out_Btn_locator.is_displayed():
            print('Sign out Element found.')
        else:
            print('Sign out Element Not found..!!')

    @allure.step("Logout from application")
    def signout_From_Application(self):
        sign_out_Btn_locator = self.browser.find_element(*self.SIGNOUT)
        sign_out_Btn_locator.click()