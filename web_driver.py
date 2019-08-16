import logging
import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Web_Driver:
    def __init__(self, destination, chromedriver_path):
        self.destination_url = destination
        self.chromedriver_path = chromedriver_path
        self.previous_scan = 0

        self.avail = 'https://driverservices.dps.mn.gov/EServices/Theme/Icon/_/Medium/Icon/Web.PendingRequests?_=795852169'
        self.not_avail = 'https://driverservices.dps.mn.gov/EServices/Theme/Icon/_/Medium/Icon/Web.Error?_=795852169'
        self.good_i = [16, 31, 46, 61, 76, 91]  # If it breaks here that's good
        logging.info('[web_driver.Web_Driver.__init__] initializing webdriver')

        try:
            self.site = webdriver.Chrome(
                executable_path=self.chromedriver_path)
            self.site.get(self.destination_url)
            # self.site.set_window_size(1200, 1000)
        except Exception as e:
            logging.error('[web_driver.Web_Driver.__init__] {}'.format(e))
    
    def close(self):
        self.site.quit()

    def prepare(self, permit_num, birth_date):
        logging.info(
            '[web_driver.Web_Driver.prepare] entering in credentials')

        time.sleep(1)
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

        time.sleep(1)
        next_button = WebDriverWait(self.site, 3).until(
            EC.presence_of_element_located((By.ID, "c-__NextStep")))
        next_button.click()

    def get_station_list(self, recursive, i):
        station_list = []

        while 1:
            try:
                time.sleep(0.15)

                main_xpath = '//*[@id="cl_c-a2-{}"]'.format(i)
                addr_xpath = '//*[@id="c-b2-{}"]'.format(i)
                avail_xpath = '//*[@id="caption2_c-d2-{}"]/img'.format(i)

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
                    'Available': False if 'Web.Error?' in station_avail else True
                }
                station_list.append(station_dict)

                logging.info(
                    '[web_driver.Web_Driver.scan_systems] added {}'.format(station_dict))
            except:
                logging.info(
                    '[web_driver.Web_Driver.scan_systems] loop ended at index {}'.format(i - 1))
                if recursive and i > 91:
                    logging.info(
                        '[web_driver.Web_Driver.scan_systems] end of full list detected')
                    return station_list
                elif recursive and i in self.good_i:
                    logging.info(
                        '[web_driver.Web_Driver.scan_systems] recursion!')
                    self.site.find_element_by_xpath(
                        '//*[@id="c-82_pgnext"]').click()
                    time.sleep(1.5)
                    station_list += self.get_station_list(True, i)
                    return station_list
                elif not recursive and i == 5:
                    logging.info(
                        '[web_driver.Web_Driver.scan_systems] end of local list detected')
                    return station_list
            i += 1

    def scan_stations(self, zip_code):
        logging.info(
            '[web_driver.Web_Driver.scan_systems] scanning available testing locations')
        self.previous_scan = time.time()

        time.sleep(0.5)
        zip_entry = self.site.find_element_by_id("c-02")
        zip_entry.send_keys(zip_code)
        zip_entry.send_keys(Keys.RETURN)

        self.local_station_list = self.get_station_list(False, 1)  # LOCAL LIST

        self.site.find_element_by_xpath('//*[@id="cl_c-42"]').click()

        self.full_station_list = self.get_station_list(True, 1)  # FULL LIST

        return self.local_station_list, self.full_station_list
