import urllib.request
import os


def download_mm(floader='ooxx',pages=10):
    os.mkdir(floder)
    os.chdir(floder)

    url=""
    page_num=int(get_page(url))

    for i in range(pages):
        page_num-=i
        page_url=url
    
