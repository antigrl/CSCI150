#! /usr/bin/python

# Write a code fragment that prompts user to enter an arbitrary number of values separated by commas and
# prints out the average of the numbers. The output should be a floating-point number.

question = raw_input ('Enter some numbers separated by commas: ')

splitSum = question.split(',')

numbers = sum(map(int,splitSum)) / float(len(splitSum))

print numbers
