from selenium_extra.driver import Driver
from selenium import webdriver


class Firefox(Driver):
    _name = "local_firefox"

    def _start_driver(self):
        return webdriver.Firefox(**self._capabilities)


class Chrome(Driver):
    _name = "local_chrome"

    def _start_driver(self):
        return webdriver.Chrome(**self._capabilities)


class Ie(Driver):
    _name = "local_IE"

    def _start_driver(self):
        return webdriver.Ie(**self._capabilities)


class Opera(Driver):
    _name = "local_Opera"

    def _start_driver(self):
        return webdriver.Opera(**self._capabilities)


class Safari(Driver):
    _name = "local_Safari"

    def _start_driver(self):
        return webdriver.Safari(**self._capabilities)


class Phantomjs(Driver):
    _name = "local_phantomjs"

    def _start_driver(self):
        return webdriver.PhantomJS(**self._capabilities)
