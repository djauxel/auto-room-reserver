import accounts

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# instantiate a chrome webbrowser
browser = webdriver.Chrome()
# navigate to the desired url
browser.get('https://biblio.csusm.edu/groupstudy/reservation_calendar.php?&login')

# finds the html id for username input
username = browser.find_element_by_id('lastname')
# finds the html id for password input
password = browser.find_element_by_id('barcode')

time.sleep(0.5) # waits for 0.5 seconds

# fills in the login form with account1's username and password
username.send_keys(accounts.account1['name'])
password.send_keys(accounts.account1['barcode'])

# finds the submit button for signing in
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
# attempts to log in by pressing the submit button
login_attempt.submit()

# TODO: figure out how to interact with the reservation table and select times