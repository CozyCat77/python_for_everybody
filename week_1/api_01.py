import urllib.request, urllib.parse, urllib.error
import json 

# target base url
base_url = 'https://random-data-api.com/api/v2/'
print("""
1.Users,
2.Address,
3.Banks,
4.Appliances,
5.Beers,
6.Blood Types,
7.Credit Cards      
""")
user_choice = input("which data would you like to access, enter the number:")
size = input("How much data would you like to receive 1-10:")
choices = ["users?", "addresses?", "banks?", "appliances?", "beers?", "blood_types?", "credit_cards?"]
url = base_url + choices[int(user_choice)] + "size=" + size 
print(url)
data = urllib.request.urlopen(url).read().decode()

res = json.loads(data)
if isinstance(res, dict):
    data_fields = list(k for k in res.keys())
    res = [res]
else:
    data_row = res[0]
    data_fields = list(k for k in data_row.keys())
for i in range(len(data_fields)):
    print(f'{i+1}:{data_fields[i]}', end=" ")
print()
user_choice = input("which information would you like to access")


# print(data_fields)
# print(data_row)
print("="*30)
for dic in res:
    el = data_fields[int(user_choice)]
    print(dic[el])
