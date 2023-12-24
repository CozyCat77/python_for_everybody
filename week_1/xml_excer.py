import urllib.request
import xml.etree.ElementTree as ET 

# url variable 
url = "https://py4e-data.dr-chuck.net/comments_1951206.xml"

# access url data and decode the data into xml
data = urllib.request.urlopen(url).read().decode()

# use xml module to transform into xml format to xml object
tree = ET.fromstring(data)

# find the count label
comments = tree.find('comments')
sum = 0
for comment in comments:
    sum += int(comment.find('count').text)
    
print(sum)