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

def getRoomID(roomNum):
    rooms = {
        "5108": "1_1",
        "5109": "2_1",
        "5302": "3_1",
        "5303": "4_1",
        "5304": "5_1",
        "5305": "6_1",
        "5306": "7_1",
        "5307": "8_1",
        "5411": "9_1",
        "4001": "11_1",
        "4002": "12_1",
        "4004": "13_1",
        "4410": "14_1",
        "2106": "15_1",
        "2107": "16_1",
        "2110": "17_1",
        "2112": "18_1",
        "2113": "19_1",
        "2116": "21_1",
        "4314": "22_1",
        "4411": "23_1",
        "4102": "27_1",
        "4103": "28_1",
        "4104": "29_1",
        "4105": "30_1",
        "4106": "31_1",
        "4107": "32_1",
        "4310": "33_1",
        "4311": "34_1",
        "4312": "35_1",
        "4313": "36_1",
        "4315": "38_1",
        "5311": "39_1",
        "5312": "40_1",
        "5313": "41_1",
        "5316": "42_1",
        "5314": "43_1",
        "5315": "44_1",
        "4306": "49_1",
        "4307": "50_1"
    }
    return rooms.get(roomNum, 'Error: invalid room index')