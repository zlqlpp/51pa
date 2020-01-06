##正则表达式
import re

p = re.compile('[0-9a-zA-Z]')
p2 = re.compile('[\u4e00-\u9fa5]+')
res = p2.findall('b315鑫鑫联系方式购买帖!')
str = ''
for i in res:
 str += i
print(str)
#print(res)
