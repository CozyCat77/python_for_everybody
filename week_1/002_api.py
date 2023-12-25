import urllib.request, urllib.parse, urllib.error
import json 

# url 
url = 'https://py4e-data.dr-chuck.net/comments_1951207.json'

# request url 
res = urllib.request.urlopen(url)
data = res.read().decode()

dict_data = (json.loads(data))

comments = dict_data['comments']
for comment in comments:
    print(comment)
    
sum = (sum(comments['count'] for comments in comments))

print(sum)