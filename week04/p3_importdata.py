# -*- coding: utf-8 -*-
import pandas as pd
# pip install xlrd
excel1 = pd.read_excel(r'1.xlsx')
excel2 = pd.read_excel(r'2.xlsx')
# print('显示的是数据总信息：-------------------------')
# print(excel1)

# 指定导入哪个Sheet
pd.read_excel(r'1.xlsx',sheet_name=0)

# 支持其他常见类型
# pd.read_csv()

import pymysql

sql = 'SELECT * FROM test.movie'
conn = pymysql.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'cy146637',
    db = 'test',
    charset ='utf8'
)
df = pd.read_sql(sql,conn)

# 1、显示整个数据表
# SELECT * FROM data;
# print(excel1)

# 2、显示整个数据表的前10行
# SELECT * FROM data LIMIT 10;
# print(excel1.head(10))

# 3、显示数据表的特定一列
# SELECT id FROM data;
# print(excel1.id)

# 4、显示数据表的数量
# SELECT COUNT(id) FROM data;
# print(excel1.(['id']).size())

# 5、显示where条件查询的数据
# SELECT * FROM data WHERE id<1000 AND age>30;
# print(excel1[(excel1.id < 1000) & (excel1.age > 30)])

# 6、显示单列和计数
# SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
# print(excel1.groupby(['num1']).size())
 
# 7、显示表1和表2的内连接
# SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
# print(pd.merge(excel1,excel2,left_on='num1',right_on='id',how='inner'))
 
# 8、 显示表1和表2合并后的数据
# SELECT * FROM table1 UNION SELECT * FROM table2;
# print(pd.concat([excel1,excel2]))

# 9、 清除表1中id等于10的值
# DELETE FROM table1 WHERE id=10;
# print(excel2.drop(excel2[excel2.id == '10'].index))
 
# 10、 修改表1，删除他某个列
# ALTER TABLE table1 DROP COLUMN column_name;
# print(excel2.drop(columns='datetime'))