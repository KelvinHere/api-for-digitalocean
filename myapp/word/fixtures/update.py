import json

with open('dictionary.json') as file:
    file = json.load(file)

for each in file:
    each['fields']['edited'] = False

with open("dictupdate.json", "w") as outfile:
    json.dump(file, outfile, indent=4,)
