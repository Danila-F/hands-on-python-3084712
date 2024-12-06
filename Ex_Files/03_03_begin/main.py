import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

with open("/workspaces/hands-on-python-3084712/Ex_Files/03_03_begin/laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


with open("/workspaces/hands-on-python-3084712/Ex_Files/03_03_begin/laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
