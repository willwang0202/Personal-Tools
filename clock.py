import time
import datetime
import sys
import os

d = datetime.datetime.now()
hourNow = d.hour
minuteNow = d.minute
secondNow = d.second

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def update():
    if hourNow < 10:
        hourOut = "0" + str(hourNow)
    else: hourOut = str(hourNow)
    if minuteNow < 10:
        minuteOut = "0" + str(minuteNow)
    else: minuteOut = str(minuteNow)
    if secondNow < 10:
        secondOut = "0" + str(secondNow)
    else: secondOut = str(secondNow)
    
    sys.stdout.write('\r' + "The current time is " + hourOut + ":" + minuteOut + ":" + secondOut + "")

past_second = secondNow
clear()
while True:
    d = datetime.datetime.now()
    hourNow = d.hour
    minuteNow = d.minute
    secondNow = d.second
    if secondNow > past_second or secondNow == 0:
        update()
        past_second = secondNow