import time
import logging
import smtplib
import sqlite3
from email.message import EmailMessage

conn = sqlite3.connect('stationdb.db')

try:
    conn.execute('''CREATE TABLE AVAILABLE
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
except sqlite3.OperationalError:
    logging.info('[data_management] sqlite3 db already exists')

conn.execute('''INSERT INTO AVAILABLE (ID,NAME,AGE,ADDRESS,SALARY) \
    VALUES (1, 'Paul', 32, 'California', 20000.00 )''')

# TODO: notify user
