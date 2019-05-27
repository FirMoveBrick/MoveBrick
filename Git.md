## Github教程

-----
- 翻墙软件（Shadowsocks）
- 快捷键t快速搜索文件
### 命令行操作git
#### 基本信息设置
1.	设置用户名
    
`git config –global user.name ‘FirMoveBrick’`

2.	设置用户名邮箱

`it config –global user.email ‘********@qq.com’`

### 初始化一个新的Git仓库

> `git init`
#### 向仓库添加文件
1.	创建文件
> 查看当前状态 `git status`

> 创建文件 `touch a1.php(文件名)`

2.	添加到暂存区

`git add as.php(文件名)`
3.	将文件从暂存区提交到仓库

`git commit -m ‘add a1.php’`

#### 修改仓库文件
1.	打开文件

 `vi a1.php(文件名)
编辑 按下ESC，  :wq保存`
2.	添加到缓存区

`git add a1.php(文件名)`
3.	将文件从暂存区提交到仓库

`git commit -m ‘第一次修改文件放到仓库中’(描述)`

#### 删除文件
1.	删除文件

`re -rf a1.php(文件名)`
2.	提出操作

`git commit -m ‘提交描述’`
3.	从Git中删除文件

`git rm a1.php(文件名)`
### Git远程仓库
* Git克隆操作
    > 目的：
将远程仓库（GitHub对应的项目）复制到本地

    `git clone 仓库地址`
    
    > 上传到远程仓库
    
    `git push`
