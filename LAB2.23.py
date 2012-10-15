#! /usr/bin/python

# Enter a date (mm/dd/yyyy) and output Day Month Year.

date = raw_input ('Enter a date (mm/dd/yyy).  ')

splitDate = date.split('/')

monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December']

fullMonth = int(splitDate[0])

day = splitDate[1]

year = splitDate[2]

month = monthNames[fullMonth -1]

print day, month, year