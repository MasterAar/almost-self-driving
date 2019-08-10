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

        self.avail = 'https://driverservices.dps.mn.gov/EServices/Theme/Icon/_/Medium/Icon/Web.PendingRequests?_=795852169'
        self.not_avail = 'https://driverservices.dps.mn.gov/EServices/Theme/Icon/_/Medium/Icon/Web.Error?_=795852169'

        houston.info('[rocket.Rocket.__init__] initializing webdriver')

        try:
            self.site = webdriver.Chrome(
                executable_path=self.chromedriver_path)
            self.site.get(self.destination_url)
            #self.site.set_window_size(1200, 1000)
        except Exception as e:
            houston.error('[rocket.Rocket.__init__] {}'.format(e))

    def prepare_boosters(self, permit_num, birth_date):
        houston.info(
            '[rocket.Rocket.prepare_boosters] entering in credentials')

        time.sleep(0.5)
        road_test_link = self.site.find_element_by_link_text(
            "Schedule or Reschedule an Exam")
        road_test_link.click()

        permit_entry = WebDriverWait(self.site, 3).until(
            EC.presence_of_element_located((By.ID, "c-8")))
        permit_entry.send_keys(permit_num)

        dob_entry = self.site.find_element_by_id("c-9")
        dob_entry.send_keys(birth_date)

        submit_button = self.site.find_element_by_id("c-__NextStep")
        submit_button.click()

        time.sleep(0.5)
        next_button = WebDriverWait(self.site, 3).until(
            EC.presence_of_element_located((By.ID, "c-__NextStep")))
        next_button.click()

    def get_station_list(self, recursive, i):
        station_list = []

        while 1:
            try:
                main_xpath = '//*[@id="cl_c-a2-{}"]'.format(i)
                addr_xpath = '//*[@id="c-b2-{}"]'.format(i)
                avail_xpath = '//*[@id="caption2_c-d2-{}"]/img'.format(i)

                print(main_xpath, addr_xpath, avail_xpath)
                station_main = WebDriverWait(self.site, 3).until(
                    EC.presence_of_element_located((By.XPATH, main_xpath)))

                station_name = station_main.text

                station_addr = self.site.find_element_by_xpath(
                    addr_xpath).get_attribute('value')

                station_avail = self.site.find_element_by_xpath(
                    avail_xpath).get_attribute('src')

                station_dict = {
                    'Station': station_name,
                    'Address': station_addr,
                    'Available': True if station_avail == self.avail else False
                }

                station_list.append(station_dict)
                houston.info(
                    '[rocket.Rocket.scan_systems] added station to list')
                print('*'*150)
                print(station_dict)
                print('*'*150)
            except:
                houston.info(
                    '[rocket.Rocket.scan_systems] loop ended at index {}'.format(i - 1))
                if i <= 2:
                    houston.warning(
                        '[rocket.Rocket.scan_systems] uncommon end index ({}), potential error occurred'.format(i - 1))
                recursive = False
                break
            i += 1

        if recursive:
            index = self.site.find_element_by_xpath(
                '//*[@id="c-82_pgof"]').text
            if int(index[0]) == 7:
                return station_list

            next_page_button = self.site.find_element_by_xpath(
                '//*[@id="c-82_pgnext"]')
            next_page_button.click()
            time.sleep(0.5)
            station_list += self.get_station_list(True, i)

        return station_list

    def scan_systems(self, zip_code):
        houston.info(
            '[rocket.Rocket.scan_systems] scanning available testing locations')
        self.previous_scan = time.time()

        time.sleep(0.5)
        zip_entry = self.site.find_element_by_id("c-02")
        zip_entry.send_keys(zip_code)
        zip_entry.send_keys(Keys.RETURN)

        self.local_station_list = self.get_station_list(False, 1)  # Local only

        show_all_button = self.site.find_element_by_xpath('//*[@id="cl_c-42"]')
        show_all_button.click()

        self.full_station_list = self.get_station_list(True, 1)  # Full scan
        print(self.full_station_list)

    def takeoff(self):
        houston.info('[rocket.Rocket.takeoff] notifying user')
        # TODO: literally everything
