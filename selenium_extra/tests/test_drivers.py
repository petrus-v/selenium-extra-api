from unittest import TestCase
from selenium_extra.drivers.local import Firefox, Chrome
from selenium_extra.drivers.remote import Grid


class TestDrivers(TestCase):

    def test_firefox(self):
        driver = Firefox.get_web_drivers({})[0]
        self.assertTrue(isinstance(driver, Firefox))
        driver.selenium.get('https://python.org')
        self.assertEquals(u"Welcome to Python.org", driver.selenium.title)
        driver.quit()

    def test_chrome(self):
        driver = Chrome.get_web_drivers({'capabilities': {}})[0]
        self.assertTrue(isinstance(driver, Chrome))
        driver.selenium.get('https://python.org')
        self.assertEquals(u"Welcome to Python.org", driver.selenium.title)
        driver.quit()

    def test_grid(self):
        driver = Grid.get_web_drivers(
            {'capabilities': {
                'command_executor': 'http://127.0.0.1:4444/wd/hub'},
                'request_drivers': [{
                    'browserName': "firefox",
                    'platform': "LINUX"}]})[0]
        self.assertTrue(isinstance(driver, Grid))
        driver.selenium.get('https://python.org')
        self.assertEquals(u"Welcome to Python.org", driver.selenium.title)
        driver.quit()
