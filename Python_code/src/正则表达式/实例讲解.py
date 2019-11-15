import re
# 实例：正则匹配.com和.cn网址
string="<a href='http://www.baidu.com'>百度首页</a>"
pat="[a-zA-Z]+://[^\s]*[.com|.cn]"
result = re.compile(pat).findall(string)
print(result)