import requests
from bs4 import BeautifulSoup

import accounts # import user accounts information

POST_LOGIN_URL = 'https://biblio.csusm.edu//groupstudy/reservation_calendar.php?=&selected_date=2019-03-30&login'
REQUEST_URL = 'https://biblio.csusm.edu/groupstudy/reservation_calendar.php?'

with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=accounts.account1)
    requestedData = session.get(REQUEST_URL)

    # print(requestedData.text)
    soup = BeautifulSoup(requestedData.text, "html.parser")
    print(soup.prettify())
    