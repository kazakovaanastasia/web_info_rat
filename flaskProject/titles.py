import requests
from bs4 import BeautifulSoup as bs

url="http://ratmania.ru/forum/index.php?topic=24863.0"
count=0
response=requests.get(url)
response.status_code
response.ok
response.headers
response.text

s={}
s=set(s)
soup=bs(response.text,'lxml')
l=len(soup.find_all("div",{"class":"poster"}))
for i in range(0,l):
    a=soup.find_all("div",{"class":"poster"})[i]
    c=a.a
    if hasattr(c, '__iter__'):
        for i in c:
                count+=1
                s.add(i)
