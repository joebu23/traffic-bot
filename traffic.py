import json
import sys
import os
from pprint import pprint

def coords(str):
	if str == "Downtown":
		return "42.961383,-85.668951"
	elif str == "M6":
		return "42.849784,-85.678554"
	elif str == "Rockford":
		return "43.11646,-85.60704"
	elif str == "Marne":
		return "3.03792,-85.82402"
	elif str == "Hudsonville":
		return "42.85899,-85.83226"
	elif str == "Cascade":
		return "42.88717,-85.49031"

url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + coords(sys.argv[1]) + "&destination=" + coords(sys.argv[2]) + "&key=AIzaSyAQxtgA3wE_Kb7kRfY26p--25RkQtDGKTE"

os.system('rm /home/media/Dev/traffic-bot/data.json')
os.system('curl -s -X GET -G -d max=300 -H "Accept: application/json" "' + url + '" >> data.json')

with open('data.json') as data_file:
	data = json.load(data_file)

print("It currently is taking " + str(data["routes"][0]["legs"][0]["duration"]["text"]) + " to get from " + sys.argv[1] + " to " + sys.argv[2])
