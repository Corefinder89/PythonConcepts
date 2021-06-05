from pages.validatelinks import Validatelinks
from utility.driverutility import Driverutility
import pytest


class Testlinks(Validatelinks, Driverutility):
    @pytest.mark.debug
    def test_link1(self):
        url = super().parse_config("project_config", "site", "site_data2")
        headless_status = super().parse_config("project_config", "browser_config", "headless_status")

        driver = super().spawn_driver("chrome", headless_status)
        super().get_url(driver, url)
