### Github pages + Hexo
 挑选Hexo模板 
[Hexo](https://hexo.io)
- 将本地图片形成MD文件链接
[sm](https://sm.ms)
- Github pages + Hexo
如何创建部署Github pages + Hexo，在这里小编是阅读朋友写的个人博客[使用 Github pages + Hexo 建立个人博客网站](https://github.com/Longgererer/Longgererer.github.io/blob/master/README.md)，十分有帮助
- 如何编写Hexo的MD文档
[编写Md文档](https://hexo.io/zh-cn/docs/)
- 小编在这里用的是[liuyib](https://github.com/liuyib/hexo-theme-stun)的hexo-theme-stun模板，感谢作者提供的主题，小编很喜欢，下面的链接是这个模板的使用手册
[hexo-theme-stun](https://liuyib.github.io/hexo-theme-stun/zh-CN/)
- 写MarkDown文档建议
如果文章路径存在中文，可能出现评论丢失的问题。因此建议将文章的 Markdown 文件用英文命名，然后将 Front-Matter 中的 title 设为文章的中文名字
- 小编在这里要特别介绍hexo-theme-stun主题里面的Bootstrap 标注
语法如下
```Bootstrap
{% note [type] [no-icon] %}
**header text**

any text
{% endnote %}
```
> 标签内可以是任意文字，支持 Markdown 和 HTML 语法

参数：
- [type]：标注类型,这里共有四种类型
 1. default（不履行）页面显示灰色
 2. success（成功） 页面显示绿色
 3. warning（警告）页面显示黄色
 4. danger（危险） 页面显示红色
- [no-icon]：是否显示 ICON（是否显示图标）

举例：
```markdown
<!-- header icon -->
{% note success %}
**Success**

This is success note.
{% endnote %}

<!-- header no-icon -->
{% note success no-icon %}
**Success**

This is success note.
{% endnote %}

<!-- no-header icon -->
{% note success %}
This is success note.
{% endnote %}

<!-- no-header no-icon -->
{% note success no-icon %}
This is success note.
{% endnote %}
```
部分效果如下
![效果图](https://i.loli.net/2019/09/27/bI4ARfy8BzhWmEs.png)




