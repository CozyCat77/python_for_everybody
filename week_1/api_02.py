import urllib.request, urllib.parse, urllib.error
import json 

# base url 
base_url = 'https://py4e-data.dr-chuck.net/json?'
# api_key auth
api_key = 42

# ask user input
address = input("Enter Location:")

url = base_url + urllib.parse.urlencode(
    {
        'key': api_key,
        'address': address
    }
)
print("Retrieving http://...")
res = urllib.request.urlopen(url)
data = res.read().decode()
print(len(data))
# into python dict
py_data = json.loads(data)

print(f'Place id {py_data['results'][0]['place_id']}')