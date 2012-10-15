#! /usr/bin/python

# Have a user input a date to tell what day of the year it is.

# Get user to input month.
questionMonth = raw_input('Enter a Month: ')

# Get user to input day.
questionDay = raw_input('Enter a Day: ')

# Capitalize month incase user provides lowercase.
questionMonth.capitalize()

# Names of the month.
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

# The number of days that are in each month (disregard leap year).
daysinMonth = [31,28,31,30,31,30,31,31,30,31,30,31]

# List suffixes for each ending number.
suffixes = ['th','st','nd','rd','th','th','th','th','th','th']

# Index user input month.
monthIndex = months.index(questionMonth)

# Days needs to start at 0.
days = 0

# For each month, days will equal days plus the number of days in the month.
for i in range(0, monthIndex):
	days = days + daysinMonth[i]

# Add the days in the month to the user input day.
days = days + int(questionDay)

# To find the last digit in days, mudulate by 10, and apply the correct suffix.
suffixIndex = days % 10

# Print user input month and day, the added up days in month and days from user, and the suffix for the days.
print questionMonth, questionDay, 'is the', str(days) + suffixes[suffixIndex], 'day', 'of the year.'