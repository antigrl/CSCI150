#! /usr/bin/python

# Find the birthstone for each month.

# Get month from user.
question = raw_input ('Please enter a Month: ')

# Capitalize first letter of month.
month = question.capitalize()

# Names of the month.
monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December']

# Birthstones for each month.
birthStones = ['Garnet','Amethyst','Aquamarine','Diamond','Emerald','Pearl','Ruby','Peridot','Sapphire','Opal','Topaz','Turquoise']

# Join the months and birthstones into a list
joinMonthStones = zip(monthNames, birthStones)

# Turn list into a dictionary.
data = dict(joinMonthStones)

# Get month name from joined MonthStones dictionary.
stone = data.get(month)

# Print birthstone for user input month.
print month + "'s", 'Birthstone is', stone + "."