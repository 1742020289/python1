import requests
from bs4 import BeautifulSoup
from lxml import etree

def openurl(url):
    r = requests.get(url, headers = headers)
    r.encoding='utf-8'
    return r.text
def downpic(url):
    name=url.split('/')[-1]
    print(url)
    picdata=requests.get(url,headers = headers)
    with  open('D:\\mztu\\'+name,'wb') as f:
        f.write(picdata.content)
first='https://www.mzitu.com/mm/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
                   'referer':'https://www.mzitu.com/196108'}
r = requests.get(first, headers = headers)
r.encoding='utf-8'
r = r.text
ehtml=etree.HTML(r)
hrefs=ehtml.xpath('//*/div[@class="postlist"]/ul[@id="pins"]/li/a/@href')
next1=ehtml.xpath('//*/div[@class="nav-links"]/a[@class="page-numbers"]/@href')
next1.insert(0,first)
page=int (input('请输入要下载的图片页数：'))
for i in  range(page):
    try:
        nextpage=openurl(next1[i])
    except IndexError:
        
        break
    nexthtml=etree.HTML(nextpage)
    hrefs=nexthtml.xpath('//*/div[@class="postlist"]/ul[@id="pins"]/li/a/@href')
    for href in hrefs:
       m= openurl(href)
       mhtml=etree.HTML(m)
       src=mhtml.xpath('//*/div[@class="main-image"]/p/a/img/@src')
       for p in src:
           downpic(p)
print('任务完成')         
#if __name__=='__main__':
  #  for nex in next1:
    #    print(nex)
       





