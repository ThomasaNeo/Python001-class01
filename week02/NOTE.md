学习笔记
1、为 Scrapy 增加代理 IP 功能，首先需要在middlewares.py中，增加代理IP类。此处类没搞懂，只是仿写了一下。
2、在使用Xpath获取网页的电影名称时，遇到了一些小状况，最后使用xpath的(string(.))方法获得电影名称。其中Xpath的.get()方法和.extract()获得内容差不多。
3、将爬取的内容保存到mysql数据库时，scrapy需要在piplines中定义数据库配置信息，settings中也同样需要增加mysql基础配置信息。