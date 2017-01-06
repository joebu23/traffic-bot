import json
import sys
from pprint import pprint

with open('data.json') as data_file:
	data = json.load(data_file)

pprint(str(data["routes"][0]["legs"][0]["duration"]["text"]))
