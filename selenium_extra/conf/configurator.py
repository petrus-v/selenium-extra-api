from selenium_extra.driver import DriverFactory
import yaml


class Configurator(object):

    config = None

    def __init__(self, path=None, yaml_conf=None):
        config = {}
        if path:
            config = yaml.safe_load(open(path))
        if yaml_conf:
            config = yaml.safe_load(yaml_conf)
        self.config = config

    def get_drivers(self):
        if not self.config:
            raise ValueError("You should define config attributes before"
                             "getting drivers instances")
        return DriverFactory().get_web_drivers(self.config)
