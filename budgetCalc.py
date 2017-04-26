# -*- coding: utf-8 -*-
import json
from datetime import datetime
from pprint import pprint

def calculate(current, desired, budget): 
	today = datetime.now()
	today = today.day
	if today > 27:
		today -= 27
	with open('budget.json') as data_file:
		data = json.load(data_file)
	for key in list(data):
		if data[key]['rec'] > 1:
			i = 0
			while i < data[key]['rec']:
				new_data = data[key]
				new_data['date'] += 7
				new_key = key + str(i)
				data[new_key] = new_data
				i += 1
		if data[key]['date'] > 27:
			data[key]['date'] -= 27
		else:
			data[key]['date'] += 3
		if today <= data[key]['date']:
			current -= data[key]['value']

	diff = current - desired
	print "You have: £%s left to spend this month" % diff

calculate(297,200,0)
