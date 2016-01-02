==================
Selenium extra API
==================

.. image:: https://api.travis-ci.org/petrus-v/selenium-extra-api.svg?branch=master
   :target: https://travis-ci.org/petrus-v/selenium-extra-api
   :alt: Travis

This is an extra api to help launcher to run the same task over multi
browsers through selenium webdrivers(local, grid, cloud provider...) session
from 1 config file.

Contribute
==========

You require chrome webdriver, firefox webdriver and a grid to run it locally

Setup local webdriver
---------------------

* **chrome**: https://sites.google.com/a/chromium.org/chromedriver/
* **firefox**: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Marionette/WebDriver


Setup grid and nodes
--------------------

https://hub.docker.com/r/selenium/
https://github.com/SeleniumHQ/docker-selenium

Running tests
-------------

.. code-block::

    virualenv sandbox
    git clone git@petrus-v/selenium-extra-api.git
    cd celenium-extra-api
    sele
    nosetests -s -v selenium_extra/tests/


State
=====

In development:
* The name of this package may change.
* no compatibility warranty over versions
* The license may change to an other OSI-approved licenses
* I may squash some commit until the first release
* Main repo can move somewhere else

TODO
====

* Allow to set several times the same config to prepare nth driver of the same
  item, mange unique id
* Rename capabilities parameter, this make thing confused
* Think about object parameter when setting remote server
* add more unittest about configuration
* documentation
* find a proper way to pass user/password...
* allow __doc__ key to comment json file (user should consider yaml files...)