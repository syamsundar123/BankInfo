import requests


BASE = "http://127.0.0.1:5000/"

branch_name = 'FORT'
limit = 3
offset = 1
city = 'BANGALORE'
response = requests.get(BASE + "api/branches/autocomplete/" + branch_name + "/" + str(limit) + "/" + str(offset))
response1 = requests.get(BASE + "api/branches/" + city + "/" + str(limit) + "/" + str(offset))
print(response.json())
print(response1.json())
#print(response2.json())