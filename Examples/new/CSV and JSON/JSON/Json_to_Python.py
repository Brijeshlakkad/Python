#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
import json
jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(jsonDataAsPythonValue)