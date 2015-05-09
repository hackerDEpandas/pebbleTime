import requests
import json
import numpy as np

# pulls data from service
s = requests.get('http://104.236.89.73:8888/project/pebble?count=True')

# decodes data into json
countData = s.json()

# return float count
x = countData['count']

# creates empty array
arr = []


for i in range(x-3):
    url = 'http://104.236.89.73:8888/project/pebble?snapshot='

    # updates page number after each iteration, and pulls data from service
    r = requests.get(url + str(3+i))

    # decodes data into json
    data = r.json()

    # grabs 'value' from 'key' 
    relevant = data['fundingDollarsRaised']

    # stores float in arr
    arr.append(relevant)
    
print arr
