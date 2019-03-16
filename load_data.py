import json
from pprint import pprint

with open('course_data.json', encoding="utf8") as f:
    data = json.load(f)["items"]

for entry in data:
    if entry["type"] == "Class":
        print(entry["id"])
