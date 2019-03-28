import accounts

def getUsername(index):
    usernames = {
        0:  accounts.account1['name'],
        1:  accounts.account2['name'],
        2:  accounts.account3['name'],
        3:  accounts.account4['name'],
        4:  accounts.account5['name']
    }
    return usernames.get(index, 'Error: invalid username index')

def getPassword(index):
    passwords = {
        0:  accounts.account1['barcode'],
        1:  accounts.account2['barcode'],
        2:  accounts.account3['barcode'],
        3:  accounts.account4['barcode'],
        4:  accounts.account5['barcode']
    }
    return passwords.get(index, 'Error: invalid password index')

def getWeekDay(weekDay):
    weekdays = {
        0:  'Mon',
        1:  'Tue',
        2:  'Wed',
        3:  'Thu',
        4:  'Fri',
        5:  'Sat',
        6:  'Sun'
    }
    return weekdays.get(weekDay, 'Error: invalid weekday index')

def getMonth(month):
    month = '0' + str(month) if month < 10 else str(month)
    return month

def getDay(day):
    day = '0' + str(day) if day < 10 else str(day)
    return day

def formatDate(month, day, abbrevWeekDay):
    currentDate = month + '/' + day + ' - ' + abbrevWeekDay
    return currentDate

def createStartID(year, month, day):
    startTime = '0830'    # 8:30am
    date = year + month + day
    startID = '1_1-' + date + startTime + '00-0'
    return startID

def createEndID(year, month, day):
    endTime = '1630'    # 4:30pm
    date = year + month + day
    endID = '1_1-' + date + endTime + '00-0'
    return endID