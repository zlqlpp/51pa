##mysql的增删改查
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

####
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      print "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
             (fname, lname, age, sex, income )
except:
   print "Error: unable to fecth data"

db.close()


# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()


# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
   cursor.execute(sql)
   db.commit()
except:
   db.rollback()

db.close()