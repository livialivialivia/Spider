connection = MySQLdb.connect(host="***",user="***",passwd="***",db="***",port=3306,charset="utf8")
cursor = connection.cursor()
sql = "*******"
sql_res = cursor.execute(sql)
connection.commit()
cursor.close()
connection.close()