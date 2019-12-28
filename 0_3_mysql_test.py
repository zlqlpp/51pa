import pymysql
 

db = pymysql.connect("127.0.0.1","root","qrkcgya520","yixian" )
cursor = db.cursor()
 

sql = """INSERT INTO qqvx( num ,url, title, date, realdate, content)
         VALUES (1, 'Mohan', 'Mohan', 'M', 'Mohan','ss')"""
try:
   cursor.execute(sql)
   db.commit()
except Exception as err:
   print(err)
   db.rollback()
 

db.close()
