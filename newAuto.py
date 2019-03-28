import accounts
import functions

import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()    # instantiate a chrome webbrowser

for i in range(0, 3):    # cycles through 5 accounts

    browser.get('https://biblio.csusm.edu/groupstudy/reservation_calendar.php?&login')    # navigate to the desired url

    username = browser.find_element_by_id('lastname')    # finds the html id for username input
    password = browser.find_element_by_id('barcode')    # finds the html id for password input

    username.send_keys(functions.getUsername(i))    # fills in the username form with an account username
    password.send_keys(functions.getPassword(i))    # fills in the password form with an account password

    login_attempt = browser.find_element_by_xpath("//*[@type='submit']")    # finds the submit button for signing in
    login_attempt.submit()    # attempts to log in by pressing the submit button

    for i in range(1, 6):    # Reserves study rooms from 0 = Monday ... 4 = Friday
        today = datetime.datetime.today()
        indexDate = today + datetime.timedelta(days = i + 1)
        year = str(today.year)
        month = functions.getMonth(indexDate.month)
        day = functions.getDay(indexDate.day)
        weekDay = indexDate.weekday()
        abbrevWeekDay = functions.getWeekDay(weekDay)
        currentDate = functions.formatDate(month, day, abbrevWeekDay)
        print(currentDate)

        browser.find_element_by_link_text(currentDate).click()

        reserveStart = browser.find_element_by_id('1_1-20190329070000-0')
        reserveStart.click()

        reserveEnd = browser.find_element_by_id('1_1-20190329073000-1')
        reserveEnd.click()
        
        reserve_attempt = browser.find_element_by_link_text('Confirm Reservation!')    # finds the html link text for confirming a reservation
        reserve_attempt.click()    # attempts to reserve a room by pressing the reserve button

        numOfAtten = browser.find_element_by_name('attendees')    # finds the html name for attendees input
        numOfAtten.send_keys(8)    # fills in the attendees form with a meaningless number

        confirm_attempt = browser.find_element_by_name('submitted')    # finds the submit button for confirming reservation
        confirm_attempt.click()    # attempts to confirm reservation by pressing the submit button

        browser.get('https://biblio.csusm.edu/groupstudy/reservation_calendar.php')    # navigate to the desired url
        
        time.sleep(20)

    logoff_attempt = browser.find_element_by_link_text('Logoff')    # finds the log off button for logging out
    logoff_attempt.click()    # attempts to log out by pressing the logoff button

# browser.find_element_by_link_text(currentDate).click()
# roomNumber = browser.find_element_by_xpath('//table/tbody/tr[1]/td[1]/div/a')
# print('Room number: ' + roomNumber.text)
# browser.find_element_by_xpath('//table/tbody/tr[1]/td[2]').click()