# almost-self-driving
Automation of Minnesota's road test registration. Searches for available testing stations and notifies the user of any availability via email (currently).
## Setting up .env
Here's an example env file:
```
PERMIT_NUM=C123456789123
ZIP=55XXX
DOB=010170
FREQ=1800
DEST=https://driverservices.dps.mn.gov/EServices/_/
CDRIVER_PATH=./chromedriver/chromedriver
EMAIL_SENDER=johnsmith@gmail.com
EMAIL_TO=johnsmithofficial@gmail.com
```
- `FREQ` is the frequency of searches (in seconds). The program will run every `FREQ` seconds.
- `CDRIVER_PATH` is the path to the ChromeDriver executable. This is not up to date with a functional Linux branch (when made, please update).
- `EMAIL_SENDER` is the email that notifications are sent from. This email needs to be configured with a Google API.
- `EMAIL_TO` is the email that notifications are sent to. This does *not need to be configued for anything.*

If you have any questions, please contact Aaron (MasterAar). This is poorly built code, and will probably fail on other machines.

## Linux specific rubbish
the chromedriver excecutable is a whiny slank and requires both excecutable permissions and additional libraries

```
chmod 775 ./chromedriver/chromedriver

apt-get install -y libglib2.0-0=2.50.3-2 \
    libnss3=2:3.26.2-1.1+deb9u1 \
    libgconf-2-4=3.2.6-4+b1 \
    libfontconfig1=2.11.0-6.7+b1
    
    ```
