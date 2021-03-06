import pymysql
pymysql.install_as_MySQLdb()

# 打开数据库连接
db = pymysql.connect("localhost", "root", "", "abilitytest", )

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行sql语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库
data = cursor.fetchone()

print("Database version : %s" % data)

# 关闭数据库连接
db.close()
