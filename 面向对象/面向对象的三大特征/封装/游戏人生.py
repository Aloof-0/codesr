# -*- coding: utf-8 -*-
# @Time    : 2019/12/3 11:04
# @Author   : 高冷
# @FileName  : 游戏人生.py


"""
练习二：游戏人生程序

1、创建三个游戏人物，分别是：

苍井井，女，18，初始战斗力1000
东尼木木，男，20，初始战斗力1800
波多多，女，19，初始战斗力2500
2、游戏场景，分别：

草丛战斗，消耗200战斗力
自我修炼，增长100战斗力
多人游戏，消耗500战斗力

"""
list_game =[]
class FOO:
    def __init__(self, name, sex, age, fight):
        self.name = name
        self.sex = sex
        self.age = age
        self.fight = fight


    def cao(self):
        self.fight -= 200

    def me(self):
        self.fight += 100
    def ppppppp(self):
        self.fight -= 500

    def shuch(self):
        print("英雄名字%s,英雄性别%s英雄年龄%s,英雄战力%s" % (self.name, self.age, self.sex, self.fight))


op = input("是否进入游戏 Y/N")
if op == "Y":
    name = input("英雄姓名")
    sex = input("男")
    age = input("年龄")
    fight = 15020
    game = FOO(name, sex, age, fight)

    list_game.append(FOO(name, sex, age, fight))
    while True:
        print("a 草丛战斗，消耗200战斗力")
        print("b 自我修炼，增长100战斗力")
        print("c 多人游戏，消耗500战斗力")
        a = input("修炼模式")
        if a == "a":
            game.cao()
            game.shuch()
        elif a == "b":
            game.me()
            game.shuch()
        elif a == "c":
            game.ppppppp()
            game.shuch()
        else:
            game.shuch()

            break






