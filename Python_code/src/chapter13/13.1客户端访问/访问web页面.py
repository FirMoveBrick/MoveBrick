import urllib.request
url ='https://www.taobao.com'
# url = input("请输入链接")
print('普通方式请求uml')
try:
    # 使用urlopen()方法发送web请求
    # result = urllib.request.urlopen(url,data= None,timeout=10)
    result = urllib.request.urlopen(url,data= None,timeout=10)
    myhtml = result.read().decode()
    myheader = result.info()
    print("输出myhtml信息")
    print(myhtml[0:800])
    print("输出myherder信息")
    print(myheader)
except urllib.error.URLError as e:
    print("无法连接服务器")
    print("错误原因",e.reason)