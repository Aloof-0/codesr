# 导入lxml 的 etree 库 (导入没有提示不代表不能用)
from lxml import etree

# 1. 利用etree.HTML,将字符串转化为Element对象,Element对象具有xpath的方法,返回结果的列表,能够接受bytes类型的数据和str类型的数据
text = ''' <div> <ul> 
        <li class="item-1"><a href="link1.html">first item你好</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a></li>
        <li><a href="link6.html"></a></li>
        </ul> </div> '''
html = etree.HTML(text=text)
# print(type(html))  # 将字符串转化为Element对象
ret_list = html.xpath("//a/text()")
# print(ret_list)


# 2.lxml能够把缺少的标签补充完成
"""
但是请注意lxml是人写的，很多时候由于网页不够规范，或者是lxml的bug，即使参考url地址对应的响应去提取数据，任然获取不到，这个时候
我们需要使用etree.tostring的方法，观察etree到底把html转化成了什么样子，即根据转化后的html字符串去进行数据的提取。
"""
text_2 = """<div> <ul> 
<li class="item-1"><a href="link1.html">first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="link5.html">fifth item</a> 
</ul> </div>
"""  # 注意，此处缺少一个 </li> 闭合标签
html_2 = etree.HTML(text_2)
handeled_html_str = etree.tostring(html).decode()  # 把转化后的element对象转化为字符串,返回bytes类型结果
# print(handeled_html_str)  # 能把缺少的标签补充完成


# 3.用lxml把html转化成字典
html3 = etree.HTML(text)
href_list = html3.xpath("//a/@href")  # 获取href的列表
title_list = html3.xpath("//a/text()")  # 获取title的列表
for i in href_list:  # 转化成href_list
    item = {}
    item["href_list"] = i
    print(item)


# 4.lxml先根据某个标签进行分组,分钟之后再进行数据的提取
text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a> 
        </ul> </div> '''
html4 = etree.HTML(text)
li_list = html.xpath("//li[@class='item-1']")
#  print("4.", li_list)
#  li_lists = li_list[0].xpath("//a/text()")  # 可以进行二次提取
# print(li_lists)
for li in li_list:  # 在每一组中继续数据的提取
    item = {}
    item["4. href"] = li.xpath("./a/@href")[0] if len(li.xpath("./a/@href"))>0 else None
    item["4. title"] = li.xpath("./a/text()")[0] if len(li.xpath("./a/text()"))>0 else None
    print(item)