# -*- coding: utf-8 -*-
# @Time    : 2020/7/21 12:23
# @Author  : Frosty
# @Email   : 935722505@qq.com
# @File    : 网站分析.py
# @Time : 2020/7/21 12:23
# @Software: PyCharm



import  requests
from bs4 import BeautifulSoup


def a():
    headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36','Host': 'movie.douban.com'}
    for i in range(0,10):
        list= []
        link = "https://movie.douban.com/top250?start="+str(i*25)+"&filter="
        r = requests.get(link,headers = headers)
        for z in range(0,10):
            print("第", str(z+1), "页的响应码", r.status_code)


        suop = BeautifulSoup(r.text,"lxml")
        div_list = suop.find_all('div', class_= 'hd')

        for each in div_list:


            movie = each.a.span.text.strip()
            list.append(movie)

        return list

movies = a()
print(movies)