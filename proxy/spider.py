import headers
import requests
from BeautifulSoup import BeautifulSoup as bs
import re
import proxyip
import time

#import sys
def spider(url):
    for head in headers.headers:
        i=0
        try:
            r = requests.get(url=url, headers=head)
            # if  r.content=="block":
            #     while r.status_code!=200:
            #         i=i+1
            #         proxy = proxyip.proxy_ip[i]
            #         r = requests.get(url=url, headers=head, proxies=proxy)
            if r.status_code != 200:
                print r.status_code
                continue
            else:
               # r = requests.get(url=url, headers=head)
                soup = bs(r.content)
                get_1 = soup.findAll(name='tr', attrs={'class': 'odd', 'id': None})
                get_2 = soup.findAll(name='tr', attrs={'class': '', 'id': None})
                con = re.findall("<td>(.*?)</td>", str(get_1))
                con+=re.findall("<td>(.*?)</td>", str(get_2))
                for i in range(0, len(con), 5):
                    # print ("%s\t%s\t%s")%(con[i],con[i+1],con[i+2])
                    check_ip(con[i],con[i+1],con[i+2],head)
                break
        except Exception,e:
            # print e
            pass
        time.sleep(0.5)


def check_ip(ip,port,type,head):
    head=head
    ip=ip
    port=port
    type=type
    proxy={ }
    proxy[type.lower()] = '%s://%s:%s'%(type.lower(),ip,port)
    try:
        check=requests.get("http://ip.cip.cc",proxies=proxy,timeout=5,headers=head)
        if ip in check.content:
            print proxy

    except Exception,e:
        pass