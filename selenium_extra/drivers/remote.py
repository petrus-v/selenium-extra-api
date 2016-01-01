from copy import deepcopy
from selenium_extra.driver import Driver
from selenium import webdriver


class Grid(Driver):

    @classmethod
    def get_web_drivers(cls, conf, global_capabilities=None):
        web_drivers = []
        if not global_capabilities:
            global_capabilities = {}
        else:
            global_capabilities = deepcopy(global_capabilities)
        capabilities = conf.get('capabilities', {})
        global_capabilities.update(capabilities)
        request_drivers = conf.get('request_drivers', [])
        for capabilities in request_drivers:
            name = 'grid'
            name = '%s_%s' % (name, capabilities.get('browserName'))
            name = '%s_%s' % (name, capabilities.get('version', 'lastest'))
            name = '%s_%s' % (name, capabilities.get('platform', 'ANY'))
            web_drivers.append(Grid(capabilities, name=name,
                                    global_capabilities=global_capabilities))
        return web_drivers

    def __init__(self, desired_capabilities, global_capabilities=None,
                 name=None):
        self.conf = desired_capabilities
        self._capabilities = global_capabilities if global_capabilities else {}
        self._capabilities.update(
            {'desired_capabilities': desired_capabilities})
        if name:
            self._name = name

    def _start_driver(self):
        return webdriver.Remote(**self._capabilities)
