#! /usr/bin/python

# Write a program that asks the user to enter two integers (separated by a space) and outputs the sum.

question = raw_input ('Enter two integers: ')

splitSum = question.split(' ')

numbers = sum(map(int,splitSum))


print 'Their sum is' , str(numbers) + '.'