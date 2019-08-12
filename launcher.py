import os
import sys
import time
import logging
from dotenv import load_dotenv
from web_driver import Web_Driver

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
w = Web_Driver(DEST, CDRIVER_PATH)

while 1:
    if time.time() - w.previous_scan > FREQ:
        w.prepare(PERMIT_NUM, DOB)

        w.scan_stations(ZIP)

        # TODO: literally everything
