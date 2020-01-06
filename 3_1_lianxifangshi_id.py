import requests
##把联系方式的  标题中的  id 提取出来，更新到表上的单独字段
from bs4 import BeautifulSoup
import pymysql
import time
import logging
import re

logging.basicConfig(filename='get_id_in_tile.log',level=logging.DEBUG)

def getidFromStr(title):
    p = re.compile('[0-9a-zA-Z]')
    res = p.findall(title)
    str = ''
    for i in res:
      str += i
    #print(str)
    return str
    
def getcnFromStr(title):
    p = re.compile('[\u4e00-\u9fa5]+')
    res = p.findall(title)
    str = ''
    for i in res:
      str += i
    #print(str)
    return str
    
db = pymysql.connect("127.0.0.1","root","qrkcgya520","yixian" )
cursor = db.cursor()

 

try:
   cursor.execute("SELECT id,title FROM qqvx_1  where title_id is null limit 10000 ")
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      title = row[1]
      #print(id, title )
      #print(getStr(title))
      su = "UPDATE qqvx_1 SET title_id='%s',title_cn='%s' WHERE id = %d" %  (getidFromStr(title),getcnFromStr(title),id)
      cursor.execute(su)
      db.commit()

      
except Exception as err:
       print(err)

db.close()

 