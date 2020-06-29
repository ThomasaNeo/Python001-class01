# -*- coding: utf-8 -*-
import scrapy
from maoyanSpiders.items import MaoyanspiderItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    # 起始URL列表
    start_urls = ['https://maoyan.com/films?showType=3']

#   注释默认的parse函数
#   def parse(self, response):
#        pass


    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象（Request）。
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def parse(self,response):
        selector=Selector(response)
        name = selector.xpath("//div[@class='movie-hover-info']/div/span[@class='name ']/text()").extract()
        mytype = selector.xpath("//div[@class='movie-hover-info']/div[2]/text()").extract()
        date = selector.xpath("//div[@class='movie-hover-info']/div[4]/text()").extract()

        print(name, mytype, date)
        item = MaoyanspiderItem()
        item['name']=name
        item['mytype']=mytype
        item['date']=date
        yield item