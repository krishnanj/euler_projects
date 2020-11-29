#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Ajay Rangarajan, Jeyashree Krishnan"
__email__ = "rangarajan, krishnan@aices.rwth-aachen.de"


import calendar
import time
"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
print time.localtime()
cal= calendar.Calendar() 
count = 0 
for year in range(1901, 2001):
	for month in range(1, 13):
		date = 0 
		for x in cal.itermonthdays(year, month):
			date = max(date, x)
		for day in range(1, date):
			val = calendar.weekday(year, month, day)
			if(val==6 and day == 1):
				count = count + 1

print count