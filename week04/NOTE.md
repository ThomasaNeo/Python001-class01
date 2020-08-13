学习笔记
1、sql中有where条件时，pandas的都会先加上该条件，语法是：table_name[table_name.col_name == '字段名'].'字段名称'
2、sql中的and条件连接是，pandas中使用&作为连接符。
3、sql中的in与not in，pandas中使用姿势：table_name[table_name.col_name.isin(['col1','col2'])]
