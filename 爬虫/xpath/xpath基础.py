# xpath基础语法练习:接下来我们听过豆瓣电影top250的页面来练习上述语法 https://movie.douban.com/top250

"""
选择所有的h1下的文本
    //h1/text()
获取所有的a标签的href
    //a/text()
获取html下的head下的title的文本
    /html/head/title/text()
获取html下的head的link标签的href
    /html/head/link@href
"""
# xpath基础语法练习2：从豆瓣电影top250的页面中：选择所有的电影的名称，href，评分，评价人数


"""
# 所有的电影的名称
//ol[@class="grid_view"]/li//span[@class="title"][1]
# 所有的电影的href
//ol[@class="grid_view"]/li//a/@href
# 所有的电影的评分
//span[@class="rating_num"]
# 所有的电影的评价人数
//div[@class="star"]/span[4]
"""
