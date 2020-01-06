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
    'O4uT_2132_saltkey': 'bTYqGpB3',
    'O4uT_2132_lastvisit': '1577322797',
    'O4uT_2132_smile': '1D1',
    'O4uT_2132_editormode_e': '-1',
    'O4uT_2132_sid': 'EyFpVJ',
    'O4uT_2132_sendmail': '1',
    'O4uT_2132_seccode': '1.1150124cd29dcdf03b',
    'O4uT_2132_ulastactivity': 'edcfgtJxiUlY4BfGTGTAhNxEssnChqt2aOFduZaHykcAicDDmWZi',
    'O4uT_2132_auth': '61852LxXMTTfYX0gsBbw%2BaNWw5zg%2FVdwobrJ0OV7c001Ei8b4jMyR416hpLRZ83SMumQByJgJGNXFbFOqOdL',
    'O4uT_2132_lastcheckfeed': '3%7C1578059053',
    'O4uT_2132_lip': '223.72.220.81%2C1578059053',
    'O4uT_2132_nofavfid': '1',
    'O4uT_2132_visitedfid': '38D36',
    'O4uT_2132_forum_lastvisit': 'D_38_1578059077',
    'O4uT_2132_st_t': '3%7C1578059081%7C8b1aece8b8b396748a79b98819d07325',
    'O4uT_2132_lastact': '1578059213%09forum.php%09ajax',
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
            ('formhash', '38a361d8'),
            ('posttime', '1578059081'),
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
           fatie('id'+id+title_cn,content)
           #print(content )
           #print(getStr(title))
           su = "UPDATE qqvx_1 SET flag='1' WHERE id = %d" %  (id)
           cursor.execute(su)
           db.commit()
     
           
     except Exception as err:
            logging.info(err)
            continue

db.close()


 