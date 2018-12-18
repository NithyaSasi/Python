'''
Created on Dec 18, 2018

@author: nithya
'''
from datetime import datetime

now = datetime.now()

mon = str(now.month)

date = str(now.day)

year = str(now.year)

hour = str(now.hour)

min = str(now.minute)

sec = str(now.second)

print (date + "/" + mon + "/" + year + " " + hour + ":" + min + ":" + sec)