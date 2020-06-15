import pytest
import allure
from pages.ContactUs import ContactUsPage


@pytest.mark.usefixtures("setup")
class TestContactUs:
    @allure.severity(severity_level="BLOCKER")
    @allure.feature("JIRA-78998 : Validate Contact Us Feature ")
    @allure.testcase("http://automationpractice.com/", "Verify Contact Us Page")
    def test_user_Registration(self):

        # Page Factory
        contact_Us_page = ContactUsPage(self.driver)

        contact_Us_page.clickOnContactUsButton()
        contact_Us_page.chooseSubjectHeading("Customer service")
        contact_Us_page.enterEmailAddress("jackson.smith@mailinator.com")
        contact_Us_page.enterMessage("Test Message Entered")
        contact_Us_page.clickOnSendButton()
        contact_Us_page.assertSucessAlert()
