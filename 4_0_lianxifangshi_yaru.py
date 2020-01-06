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



cookies = {
    'O4uT_2132_widthauto': '-1',
    'O4uT_2132_sid': 'L55861',
    'O4uT_2132_noticeTitle': '1',
    'O4uT_2132_saltkey': 'eUPJZKKo',
    'O4uT_2132_lastvisit': '1578301814',
    'O4uT_2132_sendmail': '1',
    'O4uT_2132_seccode': '2.d129df6ade0172320b',
    'O4uT_2132_ulastactivity': '6863qfLJ35MZ97k5po6JY6suWbn4yixShLhdab6KFZ%2BwBwA9fJfs',
    'O4uT_2132_auth': '6b45CQOKSaISNPvULFJgWaXWxKo4UNz9THFS0gc2NMkjyPQGCzRDhctYyhwspcaR0MxoKn1GsfbyT9NXJTin',
    'O4uT_2132_lastcheckfeed': '3%7C1578305423',
    'O4uT_2132_lip': '64.64.231.46%2C1578304954',
    'O4uT_2132_nofavfid': '1',
    'O4uT_2132_forum_lastvisit': 'D_38_1578305427',
    'O4uT_2132_visitedfid': '38',
    'O4uT_2132_st_t': '3%7C1578305473%7C91730c3f3f9cf4990da133197820db3e',
    'O4uT_2132_checkpm': '1',
    'O4uT_2132_editormode_e': '1',
    'O4uT_2132_smile': '1D1',
    'O4uT_2132_lastact': '1578305488%09forum.php%09ajax',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://dc63.cn2gia.xyz',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': 'http://dc63.cn2gia.xyz/forum.php?mod=post&action=newthread&fid=38',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

params = (
    ('mod', 'post'),
    ('action', 'newthread'),
    ('fid', '38'),
    ('extra', ''),
    ('topicsubmit', 'yes'),
)

def fatie(title1,content1):
    data = [
      ('formhash', 'dccfc34d'),
      ('posttime', '1578304099'),
      ('wysiwyg', '1'),
      ('subject', title1),
      ('message', content1),
      ('replycredit_extcredits', '0'),
      ('replycredit_times', '1'),
      ('replycredit_membertimes', '1'),
      ('replycredit_random', '100'),
      ('readperm', ''),
      ('price', '3'),
      ('tags', ''),
      ('rushreplyfrom', ''),
      ('rushreplyto', ''),
      ('rewardfloor', ''),
      ('replylimit', ''),
      ('stopfloor', ''),
      ('creditlimit', ''),
      ('allownoticeauthor', '1'),
      ('usesig', '1'),
      ('save', ''),
      ('file', ''),
      ('file', ''),
    ]
    response = requests.post('http://dc63.cn2gia.xyz/forum.php', headers=headers, params=params, cookies=cookies, data=data, verify=False)
    return 


while 1==1:
     try:
        cursor.execute(" SELECT id, title, DATE, content, title_id,title_cn FROM qqvx_1 where flag is null or flag='' order by id desc limit 100")
        results = cursor.fetchall()
        if cursor.rowcount==0:
          break
        for row in results:
           time.sleep(1)
           id = row[0]
           title = row[1]
           content = row[3]
           title_cn = row[5]
           fatie('id'+str(id)+title_cn,content)
           print(content )
           #print(getStr(title))
           su = "UPDATE qqvx_1 SET flag='1' WHERE id = %d" %  (id)
           cursor.execute(su)
           db.commit()
     
           
     except Exception as err:
            logging.info(err)
            continue

db.close()


 