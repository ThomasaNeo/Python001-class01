# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义爬虫爬取的标题、主题、上映日期
    name = scrapy.Field()
    mytype = scrapy.Field()
    date = scrapy.Field()
