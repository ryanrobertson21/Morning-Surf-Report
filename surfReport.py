#!/usr/bin/env python
#surfReport.py - Send me a text every morning of the surf conditions at Makapu'u Beach.

import requests, json, datetime, textmyself

sandysUrl = "http://magicseaweed.com/api/be85c2193e5030cc3c2c4522b4a483dc/forecast/?spot_id=984&units=us&fields=localTimestamp,swell.*"
response = requests.get(sandysUrl)

s = json.loads(response.text)

textMessage = "Morning Surf Report\nMakapu'u Beach\n"

for date in range(len(s)):
    localDate = s[date]['localTimestamp']
    localDate = datetime.datetime.fromtimestamp(int(localDate)).strftime('%Y-%m-%d %H:%M:%S')
    splitLocalDate = localDate.split(" ")
    localDateDay = splitLocalDate[0]
    localDateTime = splitLocalDate[1]
    currentDateFull = str(datetime.datetime.now())
    currentDateDay = currentDateFull.split(" ")
    timesToReport = ['08:00:00', '11:00:00', '14:00:00', '17:00:00']
    if currentDateDay[0] == localDateDay and localDateTime in timesToReport:
        # isolate the hour from military time.
        splitLocalDateTime = localDateTime.split(":")
        hour = splitLocalDateTime[0]
        # get rid of leading zeros
        if hour[0] == '0':
            earlyAmHour = hour[1]
            textMessage += str(" " + earlyAmHour + 'am' + ': ' + str(s[date]['swell']['minBreakingHeight']) + "-" + str(s[date]['swell']['maxBreakingHeight']) + ' feet\n')
        elif int(hour) > 12:
            pmHour = int(hour) - 12
            textMessage += str(" " + str(pmHour) + 'pm' + ': ' + str(s[date]['swell']['minBreakingHeight']) + "-" + str(s[date]['swell']['maxBreakingHeight']) + ' feet\n')
        else:
            textMessage += str(hour + 'am' + ': ' + str(s[date]['swell']['minBreakingHeight']) + "-" + str(s[date]['swell']['maxBreakingHeight']) + ' feet\n')

textmyself.textmyself(textMessage)



