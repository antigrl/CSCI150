#! /usr/bin/python

# If a person inputs their full first name, middle name and last name, the output will be first name, middle initial and last name.

person = raw_input ('Enter your full name. ')

names = person.split(' ')

firstName = names[0]

middleName = names[1]

lastName = names[2]

middleInital = middleName[0]

print firstName, middleInital + '.', lastName