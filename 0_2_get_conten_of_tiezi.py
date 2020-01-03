##获取贴子的内容
import requests
from bs4 import BeautifulSoup
headers = {
    'authority': 'www.vdp8.info',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'sec-fetch-user': '?1',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'referer': 'https://www.vdp8.info/forum-46-2.html',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'cookie': 'd5H4_2132_saltkey=lXRErDLD; d5H4_2132_lastvisit=1576723420; d5H4_2132_atarget=1; d5H4_2132_auth=95504%2BSA8wUWBRgJe4prTXqc%2FqrhvKUvhPXsxaLeX5ED5%2FvusvhyYeRzusEHJzb1rk61WghKHBNZ5LKpGseiWJyAVQ; d5H4_2132_lastcheckfeed=52671%7C1576743158; d5H4_2132_smile=1D1; d5H4_2132_nofavfid=1; d5H4_2132_visitedfid=46D2; d5H4_2132_forum_lastvisit=D_2_1576743198D_50_1576743207D_46_1576743215; d5H4_2132_sid=hd8MdQ; d5H4_2132_viewid=tid_52333; d5H4_2132_viewhash=cb3d4b45566ec684ad15a40d5873a073; d5H4_2132_ulastactivity=0bf4Qvovjc48zBkXW9rhUon8grnq%2BD%2BuILXXqRx%2FAFgcqeI8E2gv; d5H4_2132_sendmail=1; d5H4_2132_lastact=1576827928%09home.php%09spacecp',
}

urll = 'https://www.r4pe.info/thread-48276-1-1.html'

response = requests.get(urll, headers=headers)
#response.encoding = 'gbk'

bf = BeautifulSoup(response.text,'html.parser')
#bf = BeautifulSoup(response.text,'html5lib')

title = bf.find('a',id='thread_subject') 
print(title.text)

ems = bf.find_all('em')
print(ems[8].text)

contents = bf.find_all('td',class_='t_f')
print(contents[0].text.replace('\'',''))

#with open('/root/python3/qqvx.txt', 'wt') as f:
#    f.write(response.text)
