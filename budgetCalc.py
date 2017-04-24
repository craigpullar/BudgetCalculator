# -*- coding: utf-8 -*-
import json
from pprint import pprint

def calculate(current, desired, budget): 
	with open('budget.json') as data_file:
		data = json.load(data_file)
	for key in data:
		current -= data[key]
	diff = current - desired
	print "You have: £%s left to spend this month" % diff

calculate(2400,400,0)
