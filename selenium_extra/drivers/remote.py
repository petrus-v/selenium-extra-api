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
        grid_conf = deepcopy(conf)
        grid_conf.pop('class', None)
        request_drivers = grid_conf.pop('request_drivers', [])
        capabilities = grid_conf.pop('capabilities', {})
        global_capabilities.update(capabilities)
        for browser_req in request_drivers:
            name = 'grid'
            name = '%s_%s' % (name, browser_req.get('browserName'))
            name = '%s_%s' % (name, browser_req.get('version', 'lastest'))
            name = '%s_%s' % (name, browser_req.get('platform', 'ANY'))
            web_drivers.append(Grid(grid_conf, browser_req, name=name,
                                    global_capabilities=global_capabilities))
        return web_drivers

    def __init__(self, grid_conf, desired_capabilities,
                 global_capabilities=None, name=None):
        capab = deepcopy(global_capabilities) if global_capabilities else {}
        capab.update(desired_capabilities)
        self._capabilities = deepcopy(grid_conf)
        self._capabilities.update({
            'desired_capabilities': capab
        })
        if name:
            self._name = name

    def _start_driver(self):
        return webdriver.Remote(**self._capabilities)
