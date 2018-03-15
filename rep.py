#coding:utf-8
#将字符串中给的空格改写为20%
print '  a b '.replace(' ','20%')

import re
ret=re.compile(' ')
print ret.sub('20%','  a b ')