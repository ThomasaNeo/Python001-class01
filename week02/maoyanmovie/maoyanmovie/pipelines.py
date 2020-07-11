# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class MaoyanmoviePipeline(object):
    # def process_item(self, item, spider):
        # namemovie = item['namemovie']
        # typemovie = item['typemovie']
        # starring = item['starring']
        # datetime= item['datetime']

        # 939791997
        # output = f'|{namemovie}|\t|{typemovie}|\t|{starring}|\t|{datetime}|\n\n'
        # with open('./maoyanmovie.txt','a+',encoding='utf-8') as article:
        #     article.write(output)
        # print(output)
        # return item

    ## 打开mysql数据库
    def open_spider(self,spider):
        db = spider.settings.get('MYSQL_DB_NAME','test')
        host = spider.settings.get('MYSQL_HOST','localhost')
        port = spider.settings.get('MYSQL_PORT',3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'cy146637')

        self.db_conn = pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd)
        self.db_cur =  self.db_conn.cursor()

    # # 关闭数据库
    def close_spider(self, spider):
        self.db_conn.commit()
        self.db_conn.close()

    # # 对数据进行处理
    def process_item(self, item, spider):
        self.insert_db(item)
        return item

    # #插入数据
    def insert_db(self, item):
        values = (
            item['namemovie'],
            item['typemovie'],
            item['starring'],
            item['datetime'],
        )

        sql = 'INSERT INTO movie VALUES(%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)