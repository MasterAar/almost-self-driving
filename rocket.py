import os
import time
import logging as houston
import requests
from selenium import webdriver


class Rocket:
    def __init__(self, destination, chromedriver_path):
        self.destination_url = destination
        self.chromedriver_path = chromedriver_path
        self.previous_scan = 0

        houston.info('rocket.Rocket.__init__ initializing webdriver')

        try:
            site = webdriver.Chrome(executable_path=self.chromedriver_path)
            site.get(self.destination_url)
        except Exception as e:
            houston.error('rocket.Rocket.__init__ {}'.format(e))
        # TODO: literally everything

    def prepare_boosters(self, permit_num, birth_date):
        houston.info('rocket.Rocket.prepare_boosters entering in credentials')

    def scan_systems(self, zip_code):
        houston.info(
            'rocket.Rocket.scan_systems scanning available testing locations')
        # TODO: literally everything

        self.previous_scan = time.time()

    def takeoff(self):
        houston.info('rocket.Rocket.takeoff notifying user')
        # TODO: literally everything
