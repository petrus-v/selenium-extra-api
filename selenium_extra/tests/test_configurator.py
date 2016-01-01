from unittest import TestCase
from selenium_extra.conf.configurator import Configurator


class TestConfigurator(TestCase):

    def setUp(self):
        super(TestConfigurator, self).setUp()
        self.config = """
        drivers:
            - class: selenium_extra.drivers.local.Firefox
              capabilities:
                  __doc__: Put here Extra Firefox capabilities
            - class: selenium_extra.drivers.remote.Grid
              capabilities:
                  command_executor: http://127.0.0.1:4444/wd/hub
              request_drivers:
                  - browserName: Chrome
                    platform: Linux
                    version:
                    extra_capabilities:
                        - __doc__: Put here Extra Firefox capabilities
        global_capabilities:
            "__doc__": "Add capabilities that should be used every where"
        """
        self.config2 = """
        drivers:
            - class: selenium_extra.drivers.local.Firefox
              capabilities:
                  __doc__: Put here Extra Firefox capabilities
            - class: selenium_extra.drivers.remote.Grid
              request_drivers:
                  - browserName: Chrome
                    platform: Linux
                    version:
                    capabilities:
                        __doc__: Put here Extra Firefox capabilities
                  - browserName: Firefox
                    platform: ANY
                    version:
        global_capabilities:
            "__doc__": "Add capabilities that should be used every where"
        """

    def test_init_unexists_file(self):
        with self.assertRaises(IOError):
            Configurator(path="/this/file/does/not/exists.json")

    def test_init(self):
        conf = Configurator()
        self.assertEqual({}, conf.config)
        conf = Configurator(yaml_conf='{'
                                      '  "global_capabilities": {'
                                      '    "foo": "bar"'
                                      '  }'
                                      '}')
        self.assertEqual("bar", conf.config['global_capabilities']['foo'])
        conf = Configurator(yaml_conf="""global_capabilities:
                                            foo: bar""")
        self.assertEqual("bar", conf.config['global_capabilities']['foo'])

    def test_get_drivers(self):
        conf = Configurator(yaml_conf=self.config)
        drivers = conf.get_drivers()
        self.assertEqual(2, len(drivers))

    def test_get_drivers2(self):
        conf = Configurator(yaml_conf=self.config2)
        drivers = conf.get_drivers()
        self.assertEqual(3, len(drivers))

    def test_get_drivers_missing_class_key(self):
        conf = Configurator()
        with self.assertRaises(ValueError):
            conf.get_drivers()

    def test_get_drivers_null(self):
        conf = Configurator(yaml_conf="""
        drivers:
            - capabilities:
                  - __doc__: Put here Extra Firefox capabilities
            - class: selenium_extra.drivers.remote.grid
        """)
        with self.assertRaises(ValueError):
            conf.get_drivers()
