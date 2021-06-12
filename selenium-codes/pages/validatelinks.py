from utility.webutilty import Webutility
from utility.assertutility import Assertutility
from time import sleep


class Validatelinks(Webutility, Assertutility):

    def validate_enterprise(self, driver):
        # Get xpath for cookie decline
        xpath_decline = super().parse_config("web_config", "links", "decline_cookie")
        # Get xpath for enterprise link
        xpath_enterprise = super().parse_config("web_config", "links", "enterprise")
        # get xpath to click on who we serve
        xpath_link1 = super().parse_config("web_config", "links", "who-we-serve")

        # search elements
        web_element_enterprise = super().search_element(driver, "xpath", xpath_enterprise)
        web_element_whoweserve = super().search_element(driver, "xpath", xpath_link1)
        web_element_decline_cookie = super().search_element(driver, "xpath", xpath_decline)

        # Click element
        sleep(1)

        super().click_element(web_element_decline_cookie)
        super().click_element(web_element_whoweserve)
        super().click_element(web_element_enterprise)

        sleep(1)

        # Get actual page title
        actual_title = super().get_title(driver)
        # Get expected page title
        expected_title = super().parse_config("web_data", "assert_data", "enterprise_page_title")

        super().check_equals(actual_title, expected_title, "Actual and expected title did not match")



