import json

input = """
[
  {
        "id" : "001",
        "name" : "lisa",
        "gender": "female"
    },
    {
        "id": "002",
        "name": "rose",
        "gender": "female"
    }  
]
"""
# python loads method is to deserialize json object into python object
info = json.loads(input)
# print the len of the data 
print('User count', len(info))

for user in info:
    # access each element like a python dict
    print("id:", user['id'])
    print("name:", user['name'])
    print("gender", user['gender'])
    print("~~~~~~~~~~~~~~~~~~~~~~~~")