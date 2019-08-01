import requests
import json
from bs4 import BeautifulSoup
from twilio.rest import Client


def scrape(url):

    """
    This function scrapes the Politics section of myjoyonline.com
    a credible source of news in my homecountry, Ghana.
    """

    data = requests.get(url)
    refined = BeautifulSoup(data.text,'html.parser')
    news = refined.select('.wrapper-inner h2.entry-title')
    links = refined.select('.post-link')

    headlines = []
    anchors = []
    comb = dict()

    for x in news:
        imp = x.get_text()
        headlines.append(imp)
    #print(imp)
    #print(' ')

    for y in links:
        info = y.get('href')

    for num in range(len(headlines)):

        comb[num] = headlines[num]


    my_json = json.dumps(comb)
    return my_json


def sms(talk):
    """
    In order to see how this function is used, it would be better
    to signup with get the twilio API by signing up for
    a trial account on the twilio website.
    visit https://www.twilio.com
    There are other APIs like WhatsApp's Sandbox you could use as well
    in addition to lots of tools.


    This function sends an SMS or MMS to a number(a verified twilio number)

    """
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC5d5e141a40cd1ad612f1bbab6524374c'
    auth_token = '60d557e226be1fd70447ed6ec8697fa8'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                                  from_= '+12672142542',
                                  body = talk,
                                  to = '+14849047054'
                              )

    print(message.sid)



url = 'https://www.myjoyonline.com/ghana-news/politics.php'
solute = scrape(url)

sms(solute)
