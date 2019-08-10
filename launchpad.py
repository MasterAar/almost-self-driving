import os
import sys
import time
import logging
from dotenv import load_dotenv

file_handler = logging.FileHandler(filename='out.log')
print_handler = logging.StreamHandler(sys.stdout)
handlers = [file_handler, print_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s - %(filename)s:%(lineno)d] %(levelname)s: %(message)s',
    handlers=handlers
)

load_dotenv()
PERMIT_NUM = os.getenv('PERMIT_NUM')
ZIP_CODE = os.getenv('ZIP')
BIRTH_DATE = os.getenv('DOB')

logging.info('Starting main launcher')
logging.debug(f'{PERMIT_NUM}, {ZIP_CODE}, {BIRTH_DATE}')
