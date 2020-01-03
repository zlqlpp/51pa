##把体验报告   标题中的 id  ，匹配出来 更新到表上的 单独字段上
import requests
from bs4 import BeautifulSoup
import pymysql
import time
import logging
import re

logging.basicConfig(filename='lianxifangshi_yaru_fatie.log',level=logging.DEBUG)


db = pymysql.connect("127.0.0.1","root","qrkcgya520","yixian" )
cursor = db.cursor()


while 1==1:
     try:
        cursor.execute(" SELECT id, title, DATE, content, title_id FROM qqvx_1 where flag is null or flag='' order by id desc limit 100")
        results = cursor.fetchall()
        if cursor.rowcount==0:
          break
        for row in results:
           id = row[0]
           title = row[1]
           content = row[3]
           print(content )
           #print(getStr(title))
           #su = "UPDATE qqvx_1 SET flag='1' WHERE id = %d" %  (id)
           #cursor.execute(su)
           #db.commit()
     
           
     except Exception as err:
            logging.info(err)
            continue

db.close()


 