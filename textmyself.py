#!/usr/bin/env python
#textMyself.py - Defines the textmyself() function that texts a message passed to it as a string
from twilio.rest import TwilioRestClient

# Read in account information
with open('/Users/RyanRobertson21/PycharmProjects/CoolProjects/twilioAccountInfo') as f:
     info=f.read().splitlines()

# Preset Values
accountSID = info[0]
authToken = info[1]
myNumber = info[2]
twilioNumber = info[3]

# Send message from twilio to my number
def textmyself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)



