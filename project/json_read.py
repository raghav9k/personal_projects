import json


f = open('data.json',"r")

data = json.load(f)
names = []
print(data['recipes'][0]['name'])