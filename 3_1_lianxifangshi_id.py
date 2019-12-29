import requests
from bs4 import BeautifulSoup
import pymysql
import time
import logging
import re

logging.basicConfig(filename='lianxifangshi.log',level=logging.DEBUG)

def getStr(title):
    p = re.compile('[0-9a-zA-Z]')
    res = p.findall(title)
    str = ''
    for i in res:
      str += i
    #print(str)
    return str
    
db = pymysql.connect("127.0.0.1","root","qrkcgya520","yixian" )
cursor = db.cursor()

 
 
try:
   cursor.execute("SELECT id,title FROM qqvx_1  where title_id is null limit 100 ")
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      title = row[1]
      
      cursor.execute("UPDATE qqvx_1 SET title_id='%s' WHERE id = '%d'" % (getStr(title),id))

      
except:
   print "Error: unable to fecth data"

db.close()

 