import json

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

try: thisdict["number"] += 1
except: thisdict["number"] = 2
finally: thisdict["number"] += 1


stringified = json.dumps(thisdict, indent=4)
print(stringified)
