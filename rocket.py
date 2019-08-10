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
            self.site = webdriver.Chrome(
                executable_path=self.chromedriver_path)
            self.site.get(self.destination_url)
        except Exception as e:
            houston.error('rocket.Rocket.__init__ {}'.format(e))
        # TODO: literally everything

    def prepare_boosters(self, permit_num, birth_date):
        houston.info('rocket.Rocket.prepare_boosters entering in credentials')

        time.sleep(0.5)
        road_test_link = self.site.find_element_by_link_text(
            "Schedule or Reschedule an Exam")
        road_test_link.click()

        time.sleep(0.5)
        permit_entry = self.site.find_element_by_id("c-8")
        permit_entry.send_keys(permit_num)

        time.sleep(0.5)
        dob_entry = self.site.find_element_by_id("c-9")
        dob_entry.send_keys(birth_date)

        time.sleep(0.5)
        next_button = self.site.find_element_by_id("c-__NextStep")
        next_button.click()

        time.sleep(0.5)
        next_button = self.site.find_element_by_id("caption2_c-42")
        next_button.click()

    def scan_systems(self, zip_code):
        houston.info(
            'rocket.Rocket.scan_systems scanning available testing locations')
        self.previous_scan = time.time()
        
        time.sleep(0.5)
        zip_entry = self.site.find_element_by_id("c-02")
        zip_entry.send_keys(zip_code)

        time.sleep(0.5)
        zip_button = self.site.find_element_by_link_text("Show locations close to Zip")
        zip_button.click()
        time.sleep(1)

        # TODO: loop through available locations near ZIP, call takeoff() if necessary

        # TODO: loop through all locations, call takeoff() if necessary

    def takeoff(self):
        houston.info('rocket.Rocket.takeoff notifying user')
        # TODO: literally everything
