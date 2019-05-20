# -*- coding: utf-8 -*-
# @Time  : 2019/5/20 下午9:57
# @Author : 高杰
# @File  : main.py
# @Software: PyCharm

from scrapy.cmdline import execute

execute(["scrapy", 'crawl', 'stock', '-o', 'item.json'])
