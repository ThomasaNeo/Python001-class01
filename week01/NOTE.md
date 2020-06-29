学习笔记:
第一周作业提交测试：学习使我快乐!
学习总结：
1.使用python的虚拟环境变量时注意win与linux系统的区别
	win：python3 -m venv venv_name
	linux：python -m venv venv_name
2.vscode中运行scrapy爬虫时，容易出现引入的模板不存在，需要修改vscode的配置文件
3.使用scrapy的爬虫时，需要将settings中的ITEM_PIPELINES模块打开，否则不能将文件写入本地文件