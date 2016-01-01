import sys

from abc import ABCMeta, abstractmethod
from copy import deepcopy


class DriverFactory:

    @classmethod
    def get_web_drivers(cls, conf):
        web_drivers = []
        global_capabilities = conf.get('global_capabilities', None)
        for driver in conf['drivers']:
            if 'class' not in driver:
                raise ValueError("missing `class` key in driver config %r",
                                 driver)
            index = driver['class'].rfind('.')
            module_name = driver['class'][:index]
            class_name = driver['class'][index + 1:]
            if module_name not in sys.modules:
                __import__(module_name)
            module = sys.modules[module_name]
            driver_class = getattr(module, class_name)
            web_drivers.extend(driver_class.get_web_drivers(
                driver, global_capabilities=global_capabilities))
        return web_drivers


class Driver(object):
    __metaclass__ = ABCMeta

    _name = None
    _web_driver = None
    _capabilities = None
    conf = None
    global_capabilities = None

    @classmethod
    def get_web_drivers(cls, conf, global_capabilities=None):
        return [cls(conf, global_capabilities=global_capabilities)]

    def __init__(self, conf, global_capabilities=None, name=None):
        self.conf = conf
        self._capabilities = (deepcopy(global_capabilities) if
                              global_capabilities else {})
        self._capabilities.update(conf.get('capabilities', {}))

    @property
    def name(self):
        return self._name

    @property
    def selenium(self):
        if not self._web_driver:
            self._web_driver = self._start_driver()
        return self._web_driver

    def quit(self):
        if self._web_driver:
            self._web_driver.quit()
            self._web_driver = None

    @abstractmethod
    def _start_driver(self):
        """Abstract method that return the WebDriver instance"""
