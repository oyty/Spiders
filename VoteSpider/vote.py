# coding=utf-8
import urllib2
import threading
from time import time

"""
一旦proxy.txt有了数据，直接运行这个类就可以了，proxy里面的数据不要太多，10条左右
分散来刷
"""

# count of vote
count = 0

proxy_list = open('proxy.txt', 'r')
vote_url = 'http://www.capgn.org/tools/submit_ajax.ashx?action=vote_add&article_id=399'
timeout = 10


def add_count():
    global count
    count += 1


def get_count():
    global count
    return count


class Vote(threading.Thread):
    def __init__(self, proxy_ip):
        threading.Thread.__init__(self)
        self.url = vote_url
        self.proxy = proxy_ip

    def run(self):
        proxy_handle = urllib2.ProxyHandler({'http': self.proxy})
        opener = urllib2.build_opener(proxy_handle)
        urllib2.install_opener(opener)
        try:
            req = urllib2.urlopen(self.url)
            result = req.read()
            pos = result.find('成功')
            if pos > 1:
                print '%s vote success with proxy %s' % (result, self.proxy)
                add_count()
            else:
                print '%s vote failed with proxy %s' % (result, self.proxy)
        except Exception, e:
            print e.message, 'vote error'


if __name__ == '__main__':
    start_time = time()
    print '...starting voting'
    threads = []
    for proxy in proxy_list:
        t = Vote(proxy)
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join(timeout)  # 指定某一个线程挂起进程的最大时间

    print '%s votes have been voted successfully using %s seconds' % (get_count(), time() - start_time)
