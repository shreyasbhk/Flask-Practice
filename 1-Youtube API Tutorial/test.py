import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 645, "views": 10000, "name": "Going to the Forrest with Jake"},
        {"likes": 45, "views": 7000, "name": "Bye Bye Jake"},
        {"likes": 756, "views": 8094, "name": "Reaction to Jake"},
        {"likes": 543, "views": 74989, "name": "Apology from Jake"}]

for i in range(len(data)):
        response = requests.put(BASE + "video/" + str(i), data[i])
        print(response.json())

response = requests.delete(BASE + "video/0")
print(response)

response = requests.get(BASE + "video/2")
print(response.json())

"""
- 3
response = requests.put(BASE + "video/1", {"likes": 10, "views": 10, "name": "Going to the Forrest with Jake"})
print(response.json())
print()
response = requests.get(BASE + "video/1")
print(response)
- 2
response = requests.put(BASE + "video/1", {"likes": 10, "views": 10, "name": "Going to the Forrest with Jake"})
print(response.json())
print()
response = requests.get(BASE + "video/1")
print(response)

- 1
response = requests.get(BASE + "helloworld/tim")
"""