import os
import sys
import time
import logging as houston
from dotenv import load_dotenv
from rocket import Rocket

file_handler = houston.FileHandler(filename='out.log')
print_handler = houston.StreamHandler(sys.stdout)
handlers = [file_handler, print_handler]

houston.basicConfig(
    level=houston.DEBUG,
    format='[%(asctime)s - %(filename)s:%(lineno)d] %(levelname)s: %(message)s',
    handlers=handlers
)

load_dotenv()
PERMIT_NUM = os.getenv('PERMIT_NUM')
ZIP = os.getenv('ZIP')
DOB = os.getenv('DOB')
FREQ = int(os.getenv('FREQ'))
DEST = os.getenv('DEST')
CDRIVER_PATH = os.getenv('CDRIVER_PATH')

houston.info('Starting main launcher')
houston.debug(f'{PERMIT_NUM}, {ZIP}, {DOB}')
r = Rocket(DEST, CDRIVER_PATH)

while 1:
    if time.time() - r.previous_scan > FREQ:
        r.prepare_boosters(PERMIT_NUM, DOB)

        r.scan_systems(ZIP)

        # TODO: literally everything
