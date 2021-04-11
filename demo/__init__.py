import pymysql  # 导入驱动
# django目前只认 mysqldb python2的驱动， 但现在用的python3 将py3的驱动 pymysql  处理一下即可
pymysql.install_as_MySQLdb()
