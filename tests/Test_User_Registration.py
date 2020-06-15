import pytest
import allure
from pages.SignUp import SignUpPage
from pages.Home import HomePage


@pytest.mark.usefixtures("setup")
class TestLogin:

    @allure.severity(severity_level="BLOCKER")
    @allure.feature("JIRA-78990 : Validate user registration feature")
    @allure.testcase("http://automationpractice.com/", "Verify user registration page")
    def test_user_Registration(self):
        # Page Factory
        signup_page = SignUpPage(self.driver)
        home_page = HomePage(self.driver)

        home_page.clickOnSignInBuggon()
        signup_page.enterEmailID("jklajlkjaklklfjlajljfljlsd12@mailinator.com")
        signup_page.selectGender()
        signup_page.enterFirstName("James")
        signup_page.enterLastName("Smith")
        signup_page.enterPassword("S5CHQv@eXS8zXBq")
        signup_page.enterAddress("LinkedIn, RWC, California - USA")
        signup_page.enterCityName("RedWood City")
        signup_page.selectState("California")
        signup_page.enterZipcode("32001")
        signup_page.selectCountry("United States")
        signup_page.enterAdditionalInfo("My Office Address Deatails for reference")
        signup_page.enterMobile("5678760989")
        signup_page.address_Alias("My Home Address")
        signup_page.clickOnRegister()
        signup_page.assertSignOutAfterRegistration()
        signup_page.signout_From_Application()

        # Done with User Registration Scenario Automation
