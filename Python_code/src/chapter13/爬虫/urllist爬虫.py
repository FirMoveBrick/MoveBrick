import urllib.request  # 导入文件请求模块
import urllib.parse
from bs4 import BeautifulSoup  # 导入网页解析模块


## 定义图片下载类
class ImageDownload(object):
    def __init__(self, urlList):  # 定义构造方法
        self.urllist = urlList  # 把网页地址列表保存到实例变量中
        self.count = 0  # 标记图片数量

    def download(self, _url, name):  # 下载方法
        if (_url == None):  # 地址若为none，则返回
            return
        # print(name)
        # exit()
        try:
            result = urllib.request.urlopen(_url)  # 打开链接
            data = result.read()  # 获取图片信息
            with open(name, 'wb') as code:  # 创建文件对象
                code.write(data)  # 把图片保存到本地
                code.close()  # 关闭文件
        except urllib.error.URLError as e:  # 异常处理
            if hasattr(e, "reason"):
                print("Failed to reach the server")
                print("The reason:", e.reason)
            elif hasattr(e, "code"):
                print("The server couldn't fulfill the request")
                print("Error code:", e.code())
                print("Return content:", e.read())
            else:
                pass

    # 完成获取网页和网页解析功能
    def manager(self):
        for url in self.urllist:
            res = urllib.request.urlopen(url)  # 打开目标地址
            respond = res.read().decode()  # 获取网页地址源代码
            soup = BeautifulSoup(respond, features="html.parser")  # 实例化BeautifulSoup对象
            # print(find_all)
            # exit()
            lst = []
            for link in soup.find_all("img"):  # 获取标签为img的内容
                address = link.get('data-original')  # 获取标签属性为data-original的内容，即图片地址
                lst.append(address)  # 添加到图片列表对象list中
            s = set(lst)  # 去掉名字相同的名字
            for address in s:
                if (address != None):
                    # 设置保存图片的路径和文件名
                    pathName = "d:\\temp\\images\\" + str(self.count + 1) + ".jpg"
                    # 调用本类定义的方法进行下载
                    self.download(address, pathName)
                    # 图片累计数 + 1
                    self.count = self.count + 1
                    print("正在下载第:{0}个图片，图片名称为{1}".format(self.count, pathName))
        print('Done1')


if "__main__" == __name__:
    urlList = [
        # 'https://www.zhihu.com/question/36390957',
        # 'https://www.zhihu.com/question/28626263',
        # 'https://www.zhihu.com/question/21100397',
        # 'https://www.zhihu.com/question/23933357',
        # 'https://www.zhihu.com/question/20829553'
        'https://zhuanlan.zhihu.com/p/70878096'
    ]
    # 实例化图片下载类对象
    imgdownload = ImageDownload(urlList)
    # 调用相应方法完成下载任务
    imgdownload.manager()
