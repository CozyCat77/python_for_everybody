import sqlite3
import urllib.request
from bs4 import BeautifulSoup

conn = sqlite3.connect('userdb.sqlite')
cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS Users  
            """)

cur.execute('''
CREATE TABLE Users (
    name TEXT,
)
            ''')

# get the the url 
url = "https://py4e-data.dr-chuck.net/known_by_Montgomery.html"

# get the content from url 
html = urllib.request.urlopen(url).read()
# parse html
soup = BeautifulSoup(html, 'html.parser')
# find the li tag
tags = soup('a')
names = list()

for tag in tags:
    names.append(tag.contents[0])

for name in names:
    cur.execute('''
        INSERT INTO Users (name) VALUES (?)
                ''', (name))
    
    conn.commit()
    
query = 'SELECT * FROM Users'

for row in cur.execute(query):