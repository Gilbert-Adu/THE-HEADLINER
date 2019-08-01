# THE-HEADLINER
Web scraping mixed with SMS messaging
This python script consists of two functions: scrap and sms
As the names suggest, scrap() scrapes a news website for headlines
using the python library, requests, parses the contents of the website
using the BeautifulSoup package in python.
With a little bit of HTML manipulations, it pulls out the headlines for the day and returns
it as a JSON.

The function sms() makes use of the cloud communications API, Twilio to send headlines received 
in the form of JSON from one phone number to another.

#REQUIREMENTS FOR BUILDING SOMETHING SIMILAR:
1. Python or Preferred language: Java, Curl, Ruby etc
2. Get a Twilio account. P.S: They have free trials..get one of those
3. Make sure you install twilio from your directory using the 'pip install twilio command'. If this doesn't work, 
visit the official twilio website. Visit www.twilio.com for information.

Enjoy!
