import json
from json import JSONDecodeError, JsonEncoder

jsonString = '{"a": 1, "b": 2, "c": 3}'
try:
  jsonData = json.loads(jsonString)
except json.JSONDecodeError as e:
  print(f"Error: {e}")

print(jsonData)

pythonDict = {
  'a': 1,
  'b': 2,
  'c': 3
}

jsonString1 = json.dumps(pythonDict, indent=4)
print(jsonString1)


