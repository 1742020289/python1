import requests
from lxml import etree
import re
import os
def getpic(url):
    name=mmurl.split('/')[-1]
    print(name)
    picdata=requests.get(url)
    with  open('D:\\mzsock\\'+name,'wb') as f:
        f.write(picdata.content)
r=requests.get("http://mzsock.com/mv/")
r.encoding='utf-8'
r=r.text
ehtml=etree.HTML(r)
nurl=ehtml.xpath('//*/li/div/a[@class="img"]/@href')
for mz in nurl:
    mm=requests.get(mz)
    mm.encoding='utf-8'
    mm=mm.text
    mhtml=etree.HTML(mm)
    murl=mhtml.xpath('//*/a[@class="image_cx_cont"]/img/@src')

    for mmurl in murl:
        getpic(mmurl)
        

    

                 




