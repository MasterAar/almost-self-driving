# almost-self-driving
Automation of Minnesota's road test registration. Searches for available testing stations and notifies the user of any availability via email (currently). Because of a lack of time, I will not write that much documentation, especially concerning the Google/Gmail API, however a brief summary of the environment variables are described below.
When executed, the script will only email the user when necessary, that is, when the stations nearby one's ZIP code are available. As I passed the test already, I cannot help with development of this program anymore, but feel free to add on more features (say, listing stations by distance from the user's current location, or auto-signing up after verifying that there are open spots).
## Setting up .env
Here's an example env file:
```
PERMIT_NUM=C123456789123
ZIP=55XXX
DOB=010170
FREQ=1800
DEST=https://driverservices.dps.mn.gov/EServices/_/
CDRIVER_PATH=.\chromedriver\chromedriver.exe
EMAIL_SENDER=johnsmith@gmail.com
EMAIL_TO=johnsmithofficial@gmail.com
```
- `FREQ` is the frequency of searches (in seconds). The program will run every `FREQ` seconds.
- `CDRIVER_PATH` is the path to the ChromeDriver executable. This is not up to date with a functional Linux branch (when made, please update).
- `EMAIL_SENDER` is the email that notifications are sent from. This email needs to be configured with a Google API.
- `EMAIL_TO` is the email that notifications are sent to. This does *not need to be configued for anything.*

If you have any questions, please contact Aaron (MasterAar). This is poorly built code, and will probably fail on other machines.
