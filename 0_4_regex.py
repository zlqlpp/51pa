import re

p = re.compile('[0-9a-zA-Z]')
res = p.findall('b315鑫鑫联系方式购买帖!')
str = ''
for i in res:
 str += i
print(str)
#print(res)
