# 用get方法提交表单实例
import urllib.request
import urllib.parse


def addGetData(url, data):  # 定义编码函数
    return url + '?' + urllib.parse.urlencode(data)


url = 'https://www.wunderground.com/weather/cn/beijing'
zipcode = '30301'
# myUrl = addGetData(url, [('query', zipcode)])  # 生成url
# url1 ='https://www.taobao.com'
print('使用get方式请求url')
try:
    result = urllib.request.urlopen(url, data=None, timeout=10)
    myhtml = result.read().decode()
    myheader = result.info()
    print('输出myhtml信息')
    print(myhtml[1:300])
    f = open('d://temp//myhtml.html', 'w')
    f.write(myhtml)
    f.close()
    print('输出myherder信息')
    print(myheader)
except urllib.error.URLError as e:
    print("无法连接服务器")
    print("错误原因",e.reason)
