import json
from pprint import pprint

with open('course_data.json', encoding="utf8") as f:

    data = json.load(f)

pprint(data)

#open('data.txt', encoding="utf8").read()