# -*- coding: utf-8 -*-
import json
from datetime import datetime
from pprint import pprint

def calculate(current, desired, budget): 
	today = datetime.now()
	today = today.day
	today = 1
	if today > 27:
		today -= 27
	with open('budget.json') as data_file:
		data = json.load(data_file)
	for key in data:
		if data[key]['date'] > 27:
			data[key]['date'] -= 27
		else:
			data[key]['date'] += 3
		if today <= data[key]['date']:
			current -= data[key]['value']
	diff = current - desired
	print "You have: £%s left to spend this month" % diff

calculate(656,400,0)
