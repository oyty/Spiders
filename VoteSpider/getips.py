# coding=utf-8
__author__ = 'oyty'
import getipfuns

"""
    配置文件
"""

strategys = {
    'stategy_haodaili': {
        'base_url': 'http://www.haodailiip.com/guonei/',
        'start_page': 1,
        'end_page': 3,
        'page_hrs':30,
        'method': 'haodaili_proxys'
    },
    'strategy_haodaili': {
        'base_url': 'http://www.kuaidaili.com/proxylist/',
        'start_page': 1,
        'end_page': 5,
        'page_hrs':10,
        'method': 'kuaidaili_proxys'
    }
}
strategy_num = 0
strategy = strategys.get('strategy_haodaili')


def execute(fun, *args):
    fun(args[0], args[1])


if __name__ == '__main__':
    start_page = int(strategy.get('start_page'))
    end_page = int(strategy.get('end_page'))
    execute(getattr(getipfuns, strategy.get('method')), start_page, end_page)
