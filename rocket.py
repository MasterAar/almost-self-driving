import os
import time
import logging as houston
import requests
import selenium


class Rocket:
    def __init__(self, destination):
        self.destination_url = destination

        houston.info('rocket.Rocket.__init__ initializing webdriver')
        # site = webdriver.Chrome()
        # site.get(self.destination_url)
        # TODO: literally everything

    def prepare_boosters(self, permit_num, birth_date):
        houston.info('rocket.Rocket.prepare_boosters entering in credentials')

    def scan_systems(self, zip_code):
        houston.info(
            'rocket.Rocket.scan_systems scanning available testing locations')
        # TODO: literally everything

        self.previous_scan

    def takeoff(self):
        houston.info('rocket.Rocket.takeoff notifying user')
        # TODO: literally everything
