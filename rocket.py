import os
import time
import logging as houston
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Rocket:
    def __init__(self, destination, chromedriver_path):
        self.destination_url = destination
        self.chromedriver_path = chromedriver_path
        self.previous_scan = 0

        houston.info('[rocket.Rocket.__init__] initializing webdriver')

        try:
            self.site = webdriver.Chrome(
                executable_path=self.chromedriver_path)
            self.site.get(self.destination_url)
            #self.site.set_window_size(1200, 1000)
        except Exception as e:
            houston.error('[rocket.Rocket.__init__] {}'.format(e))

    def prepare_boosters(self, permit_num, birth_date):
        houston.info('[rocket.Rocket.prepare_boosters] entering in credentials')

        time.sleep(0.5)
        road_test_link = self.site.find_element_by_link_text(
            "Schedule or Reschedule an Exam")
        road_test_link.click()

        time.sleep(0.5)
        permit_entry = self.site.find_element_by_id("c-8")
        permit_entry.send_keys(permit_num)

        dob_entry = self.site.find_element_by_id("c-9")
        dob_entry.send_keys(birth_date)

        next_button = self.site.find_element_by_id("c-__NextStep")
        next_button.click()

        time.sleep(0.5)
        next_button = self.site.find_element_by_id("c-__NextStep")
        next_button.click()

    def scan_systems(self, zip_code):
        houston.info(
            '[rocket.Rocket.scan_systems] scanning available testing locations')
        self.previous_scan = time.time()

        time.sleep(0.5)
        zip_entry = self.site.find_element_by_id("c-02")
        zip_entry.send_keys(zip_code)
        zip_entry.send_keys(Keys.RETURN)

        i = 1
        while 1:
            try:
                station_id = 'cl_c-a2-' + str(i)
                element = WebDriverWait(self.site, 3).until(
                    EC.presence_of_element_located((By.ID, station_id)))
                print(type(element))
            except:
                i -= 1
                houston.info('[rocket.Rocket.scan_systems] last testing location found, index {}'.format(i))
                break
            i += 1

    def takeoff(self):
        houston.info('[rocket.Rocket.takeoff] notifying user')
        # TODO: literally everything
