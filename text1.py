import requests
from bs4 import BeautifulSoup as bs
import os
def getpic(url):
    name=d['src'].split('/')[-1]
    print(name)
    picdata=requests.get(url)
    with  open('D:\\mzsock\\'+name,'wb') as f:
        f.write(picdata.content)

url='http://mzsock.com/mv/'
r=requests.get(url)
r=r.text
all_a=bs(r,'lxml').find('ul',id='post-list').find_all('a')
for a in all_a:
    mm=requests.get(a['href'])
    mm=mm.text
    durl=bs(mm,'lxml').find('div',class_="picsbox picsboxcenter chenxing_pic_images").find_all('img')
    
    for d in durl:
        
        getpic(d['src'])
      
     
        

