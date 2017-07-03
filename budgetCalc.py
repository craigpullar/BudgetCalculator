# -*- coding: utf-8 -*-
import json
from datetime import datetime
from pprint import pprint

def calculate(current, desired, budget): 
	today = datetime.now()
	today = today.day
	if today > 27:
		today -= 27
	else:
		today += 3
	with open('budget.json') as data_file:
		data = json.load(data_file)
	
	for key in list(data):
		if data[key]['date'] > 27:
			data[key]['date'] -= 27
		else:
			data[key]['date'] += 3
	for key in list(data):
		if data[key]['rec'] > 1:
			print data[key]
			i = 1
			while i < data[key]['rec']:
				new_key = key + str(i)
				new_date = data[key]['date'] + (7*i)
				data[new_key] = {'date' : new_date, 'rec' : 1, 'value' : data[key]['value']}
				i += 1
	for key in list(data):
		if data[key]['date'] > today:
			print key
			print data[key]
	for key in list(data):
		if today <= data[key]['date']:
			current -= data[key]['value']
			diff = current - desired
	print "You have: £%s left to spend this month" % diff

calculate(929,0,0)
