# coding=utf-8
import urllib2

"""
一旦proxy.txt有了数据，直接运行这个类就可以了，proxy里面的数据不要太多，10条左右
分散来刷
"""

proxylist = open('proxy.txt', 'r')
url = 'http://www.capgn.org/tools/submit_ajax.ashx?action=vote_add&article_id=399'
timeout = 1000


def handle(proxy):
    proxy_handle = urllib2.ProxyHandler({'http': proxy})
    opener = urllib2.build_opener(proxy_handle)
    urllib2.install_opener(opener)
    try:
        req = urllib2.urlopen(url)
        result = req.read()
        print result
        pos = result.find('成功')
        if pos > 1:
            print 'VoteSpider success --- %s' % proxy
        else:
            print 'VoteSpider failed --- %s' % proxy
    except Exception, e:
        print e.message, 'error'


if __name__ == '__main__':
    for proxy in proxylist:
        handle(proxy)
