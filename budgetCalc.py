# -*- coding: utf-8 -*-
import json
from datetime import datetime
from pprint import pprint

def calculate(current, desired, budget): 
	today = datetime.now()
	today = today.day
	with open('budget.json') as data_file:
		data = json.load(data_file)
	for key in data:
		if data[key]['date'] < 27 and today <= data[key]['date']:
			current -= data[key]['value']
		elif today >= 27 and today <= data[key]['date'] and data[key]['date'] >= 27:
			current -= data[key]['value']
	diff = current - desired
	print "You have: £%s left to spend this month" % diff

calculate(2400,400,0)
