import os
import time
import logging as houston
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

permit_num = 'C000028397000'
birth_date = '08302002'
site = webdriver.Chrome(executable_path='.\chromedriver\chromedriver.exe')
site.get('https://driverservices.dps.mn.gov/EServices/_/')

time.sleep(0.5)
road_test_link = site.find_element_by_link_text(
    "Schedule or Reschedule an Exam")
road_test_link.click()
time.sleep(0.5)
permit_entry = WebDriverWait(site, 3).until(EC.presence_of_element_located((By.ID, "c-8")))
#permit_entry = site.find_element_by_id("c-8")
permit_entry.send_keys(permit_num)
dob_entry = site.find_element_by_id("c-9")
dob_entry.send_keys(birth_date)
next_button = site.find_element_by_id("c-__NextStep")
next_button.click()
time.sleep(0.5)
next_button = WebDriverWait(site, 3).until(EC.presence_of_element_located((By.ID, "c-__NextStep")))
#next_button = site.find_element_by_id("c-__NextStep")
next_button.click()

i = 1
main_xpath = '//*[@id="cl_c-a2-{}"]'.format(i)
addr_xpath = '//*[@id="c-b2-{}"]'.format(i)
avail_xpath = '//*[@id="caption2_c-d2-{}"]/img'.format(i)

available = 'https://driverservices.dps.mn.gov/EServices/Theme/Icon/_/Medium/Icon/Web.PendingRequests?_=795852169'
not_avail = 'https://driverservices.dps.mn.gov/EServices/Theme/Icon/_/Medium/Icon/Web.Error?_=795852169'

print(main_xpath, addr_xpath, avail_xpath)

station_main = WebDriverWait(site, 3).until(
    EC.presence_of_element_located((By.XPATH, main_xpath)))
station_main.click()
station_name = station_main.text

station_addr = site.find_element_by_xpath(addr_xpath).get_attribute('value')

station_avail = site.find_element_by_xpath(avail_xpath).get_attribute('src')
if station_avail == available:
    print('AVAILABLE')
elif station_avail == not_avail:
    print('NO')
print(station_name, station_addr, station_avail)