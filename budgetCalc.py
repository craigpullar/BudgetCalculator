import json
from pprint import pprint

def calculate(current, desired, budget): 
	with open('budget.json') as data_file:
		data = json.load(data_file)
		pprint(data)
	return 0;

calculate(0,0,0)
