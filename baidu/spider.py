import headers
import requests
import BeautifulSoup
import re
import sys
def spider(url):
    for i in headers.headers:
        try:
            r = requests.get(url=url, headers=i)
            if r.status_code != 200:
                print r.status_code
                continue
            else:
                soup=BeautifulSoup.BeautifulSoup(r.content)
                url_all=soup.findAll(name='a',attrs={'target':'_blank','data-click':re.compile('.'),'class':None})
                for url_one in url_all:
                    url_baidu=url_one['href']
                    url_relay=requests.get(url=url_baidu,headers=i)
                    print ("%s\n%s")%(url_relay.url,url_one.text)
                break
        except Exception,e:
            pass
