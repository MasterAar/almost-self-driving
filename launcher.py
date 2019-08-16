import logging
import os
import sys
import time

from dotenv import load_dotenv

from web_driver import Web_Driver

import comms

file_handler = logging.FileHandler(filename='out.log')
print_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, print_handler]

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s - %(levelname)s] %(message)s',
    handlers=handlers
)

load_dotenv()
PERMIT_NUM = os.getenv('PERMIT_NUM')
ZIP = os.getenv('ZIP')
DOB = os.getenv('DOB')
FREQ = int(os.getenv('FREQ'))
DEST = os.getenv('DEST')
CDRIVER_PATH = os.getenv('CDRIVER_PATH')

logging.info('Starting main launcher')
logging.debug(f'{PERMIT_NUM}, {ZIP}, {DOB}')


while 1:
    if time.time() - w.previous_scan > FREQ:
        w = Web_Driver(DEST, CDRIVER_PATH)
        time.sleep(0.5)
        w.prepare(PERMIT_NUM, DOB)
        local_list, full_list = w.scan_stations(ZIP)

        '''
        local_list = [{'Station': 'Walker Exam Station', 'Address': '701 ELM ST WALKER MN 56484', 'Available': True}, {'Station': 'Warren Exam Station', 'Address': '208 E COLVIN AVE MN 56762', 'Available': True}, {'Station': 'Waseca Exam Station', 'Address': '300 N STATE ST MN 56093', 'Available': False}, {
            'Station': 'Wheaton Exam Station', 'Address': '702 2ND AVE N MN 56296', 'Available': True},
            {'Station': 'Willmar Exam Station',
                'Address': '1601 E HWY 12 MN 56201', 'Available': False},
            {'Station': 'Windom Exam Station',
                'Address': '1012 5TH AVE RM 20 WINDOM MN 56101', 'Available': False}
        ]
        '''

        available_list = []
        for station in local_list:
            if station['Available']:
                available_list.append(station)

        if len(available_list) == 0:
            for station in full_list:
                if station['Available']:
                    available_list.append(station)

        if len(available_list) > 0:
            body = f'There are {len(available_list)} stations available!\n\n'

            for station in available_list:
                body += (f'{station["Station"]} at {station["Address"]}\n')

            print(body)
            comms.send_email("DRIVER'S TEST LOCATIONS", body)
    time.sleep(1)
