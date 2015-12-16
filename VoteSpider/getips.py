# coding=utf-8
__author__ = 'oyty'
import getipfuns

"""
    配置文件
"""

"""
    以下是两种获取代理ip的策略，也就是两个网站,你可以任选一种获取ip
"""
strategys = {
    'stategy_haodaili': {
        'base_url': 'http://www.haodailiip.com/guonei/',  # 代理ip获取的网址
        'start_page': 1,  # 获取代理ip的起始页  这个地方可以自行修改
        'end_page': 3,  # 获取代理ip的终止页   这个地方可以自行修改
        'page_hrs': 30,  # 表示一页有30条ip数据
        'method': 'haodaili_proxys'
    },
    'strategy_kuaidaili': {
        'base_url': 'http://www.kuaidaili.com/proxylist/',
        'start_page': 1,  # 获取代理ip的起始页  这个地方可以自行修改
        'end_page': 5,  # 获取代理ip的终止页   这个地方可以自行修改
        'page_hrs': 10,
        'method': 'kuaidaili_proxys'
    }
}
strategy_num = 0

"""
    strategy_choose配置你要选择的策略，由上面可以知道
    这两种策略为strategy_haodaili，strategy_kuaidaili
"""
strategy_choose = 'strategy_kuaidaili' # 这个地方可以自行修改
strategy = strategys.get(strategy_choose)


def execute(fun, *args):
    fun(args[0], args[1])


if __name__ == '__main__':
    start_page = int(strategy.get('start_page'))
    end_page = int(strategy.get('end_page'))
    execute(getattr(getipfuns, strategy.get('method')), start_page, end_page)
