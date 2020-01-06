##把体验报告   标题中的 id  ，匹配出来 更新到表上的 单独字段上
import requests
from bs4 import BeautifulSoup
import pymysql
import time
import logging
import re
import xlrd
import xlwt
import openpyxl

logging.basicConfig(filename='huisuo_yaru_fatie.log',level=logging.DEBUG)

cookies = {
    'O4uT_2132_saltkey': 'sJjGiwbH',
    'O4uT_2132_lastvisit': '1576580352',
    'O4uT_2132_seccode': '3.d6a10ad09697aea06d',
    'O4uT_2132_ulastactivity': '1db5kC1dG21g2lxRaZTCC5y9pUwSEcRhoziZWF1N%2BYtqOwZIes5R',
    'O4uT_2132_auth': 'a34bEMZ%2FcKy5F%2FttQb19nOVeixWlGMWZZbLHg5EfdmirsPOWoWlVcdSuciAh80gUGhc5gcOaqcsHwY0cFWme',
    'O4uT_2132_lastcheckfeed': '3%7C1578319617',
    'O4uT_2132_editormode_e': '1',
    'O4uT_2132_smile': '1D1',
    'O4uT_2132_nofocus_forum': '1',
    'O4uT_2132_st_p': '3%7C1578321303%7Cb5cc9ab48de5353152752829e5bda5e4',
    'O4uT_2132_viewid': 'tid_6439',
    'O4uT_2132_nofavfid': '1',
    'O4uT_2132_forum_lastvisit': 'D_38_1578321300D_40_1578323475',
    'O4uT_2132_visitedfid': '40D38',
    'O4uT_2132_checkpm': '1',
    'O4uT_2132_sendmail': '1',
    'O4uT_2132_st_t': '3%7C1578323477%7C71f7fdf815534bcc09b96324ba3ba45b',
    'O4uT_2132_sid': 'g11tv0',
    'O4uT_2132_lip': '64.64.231.46%2C1578323497',
    'O4uT_2132_lastact': '1578323497%09forum.php%09ajax',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'http://dc63.cn2gia.xyz',
    'Upgrade-Insecure-Requests': '1',
    'DNT': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://dc63.cn2gia.xyz/forum.php?mod=post&action=newthread&fid=40',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
}

params = (
    ('mod', 'post'),
    ('action', 'newthread'),
    ('fid', '40'),
    ('extra', ''),
    ('topicsubmit', 'yes'),
)

def fatie(title1,content1):
       data = [
         ('formhash', '541086cc'),
         ('posttime', '1578323477'),
         ('wysiwyg', '1'),
         ('subject', 'aaaaaaa'),
         ('message', 'bbbbbbbbbbbb\r\n'),
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
       print(title1,content1 )
       #print(res.text)
       return 

def read03Excel(path):
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    worksheet = workbook.sheet_by_name(sheets[0])
    for i in range(0, worksheet.nrows):
        row = worksheet.row(i)
        #for j in range(0, worksheet.ncols):
        #    print(worksheet.cell_value(i, j), "\t", end="")
        #print()
        print(worksheet.cell_value(i, 0)+worksheet.cell_value(i, 1)+worksheet.cell_value(i, 2)+worksheet.cell_value(i, 3)+worksheet.cell_value(i, 5))
        title1 = worksheet.cell_value(i, 0)+worksheet.cell_value(i, 1)+worksheet.cell_value(i, 2)+worksheet.cell_value(i, 3)+worksheet.cell_value(i, 5)
        content1 = = worksheet.cell_value(i, 4)+worksheet.cell_value(i, 6)
        fatie(title1,content1)
 

read03Excel('/root/lllllffffff.xls')
 