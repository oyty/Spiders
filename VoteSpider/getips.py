# -*- coding:utf8 -*-
import requests
import time
from BeautifulSoup import BeautifulSoup

"""
这个方法是获取可用的国内代理ip，可以登入http://www.haodailiip.com/guonei/查看
for i in range(4, 5): 主要在range里面进行修改，可以对着网站上的看，一页有三十条数据
所以一次最好获取一页数据，range(5, 6)表示获取第四页数据，以此类推
"""

of = open('proxy.txt', 'w')
url = 'http://www.haodailiip.com/guonei/'
for i in range(5, 6):
    Url = 'http://www.haodailiip.com/guonei/' + str(i)
    print "正在采集" + Url
    html = requests.get(Url).text
    bs = BeautifulSoup(html)
    table = bs.find('table', {"class": "proxy_table"})
    tr = table.findAll('tr')
    for i in range(1, 31):
        td = tr[i].findAll('td')
        proxy_ip = td[0].text.strip()
        proxy_port = td[1].text.strip()
        of.write('%s:%s\n' % (proxy_ip, proxy_port))
        print '%s:%s\n' % (proxy_ip, proxy_port)
    time.sleep(2)
    of.closed
