# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanmovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    namemovie = scrapy.Field()
    typemovie = scrapy.Field()
    starring = scrapy.Field()
    datetime = scrapy.Field()