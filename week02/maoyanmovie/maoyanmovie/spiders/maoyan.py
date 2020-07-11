# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyanmovie.items import MaoyanmovieItem
import pandas as pd

data = pd.DataFrame()
class MaoyanSpider(scrapy.Spider):
    # 定义爬虫名称
    name = 'maoyan'
    # 爬虫允许的URL列表
    allowed_domains = ['maoyan.com']
    # 爬虫的起始列表
    start_urls = ['https://maoyan.com/films?showType=3']

    # 爬虫启动时，引擎自动调用的方法，并且只调用一次，用于生成初始化的请求对象（Request）。
    # start_requests()方法获取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页。
    def start_requests(self):
        url = f'https://maoyan.com/films?showType=3'
        # callback回调函数，引擎会将下载好的页面(Response对象)发送给该方法，执行数据解析
        # callback指定新的函数，不是用parse作为默认的回调函数
        yield scrapy.Request(url=url,callback=self.parse,dont_filter=True)   

    def parse(self,response):
        items = []
        movies = Selector(response=response).xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd/div[1]/div[2]/a/div')
        for movie in movies:
            if len(data) > 9:
                break       
            item = MaoyanmovieItem()
            movietitle = movie.xpath('./div/span')
            text2 = movie.xpath('./div/text()')

            item['namemovie'] = movietitle.xpath('string(.)').get()
            item['typemovie'] = text2.extract()[4].strip()
            item['starring'] = text2.extract()[6].strip()
            item['datetime'] = text2.extract()[8].strip()

            items.append(item)
            print(movietitle.xpath('string(.)').get())
            print(text2.extract()[4].strip())
            print(text2.extract()[6].strip())
            print(text2.extract()[8].strip())
            print(items)
            return items

    