# -*- coding:utf8 -*-
import requests
import getips
import time
from BeautifulSoup import BeautifulSoup

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

"""
这个方法是获取可用的国内代理ip，可以登入http://www.haodailiip.com/guonei/查看
for i in range(4, 5): 主要在range里面进行修改，可以对着网站上的看，一页有三十条数据
所以一次最好获取一页数据，range(5, 6)表示获取第四页数据，以此类推
"""

of = open('proxy.txt', 'w')
base_url = getips.strategy.get('base_url')


def haodaili_proxys(start_page, end_page):
    for i in range(start_page, end_page):
        url = base_url + str(i)
        print "正在采集" + url
        html = requests.get(url).text
        bs = BeautifulSoup(html)
        table = bs.find('table', {"class": "proxy_table"})
        tr = table.findAll('tr')
        for i in range(0, int(getips.strategy.get('page_hrs'))):
            td = tr[i].findAll('td')
            proxy_ip = td[0].text.strip()
            proxy_port = td[1].text.strip()
            of.write('%s:%s\n' % (proxy_ip, proxy_port))
            print '%s:%s\n,' % (proxy_ip.decode('utf-8'), proxy_port.decode('utf-8'))
        time.sleep(2)
    of.close()


def kuaidaili_proxys(start_page, end_page):
    for i in range(start_page, end_page):
        url = base_url + str(i)
        print "正在采集" + url
        html = requests.get(url).text
        bs = BeautifulSoup(html)
        table = bs.find('tbody')
        tr = table.findAll('tr')
        for i in range(0, int(getips.strategy.get('page_hrs'))):
            td = tr[i].findAll('td')
            proxy_ip = td[0].text.strip()
            proxy_port = td[1].text.strip()
            of.write('%s:%s\n' % (proxy_ip, proxy_port))
            print '%s:%s' % (proxy_ip, proxy_port)
        time.sleep(2)
    of.close()
