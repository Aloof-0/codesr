# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/2 14:16
@Auth ： 高冷Aloof
@File ：serializses.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# 针对BookInfo模块类对象,定义一个序列化器,这个序列化专门用来操作BookInfo 对象
# (1). 明确操作的目标数据  -- 模型类
# (2). 继承自serializer
# (3). 定义和模型类"同名"类属性, 类型 --- 对应的形式. 来确定参与序列号模型类属性
# (4).
#  serializers模块
from rest_framework import serializers


class BookInfoserializer(serializers.Serializer):
    btitle = serializers.CharField(max_length=20)
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()
    is_delete = serializers.BooleanField()
    image = serializers.ImageField()
    # 1.序列化为关联对象的主键值,read_only=True表明此属性/字段只参与序列化操作
    book_pk = serializers.PrimaryKeyRelatedField(read_only=True)
    # 2.序列化为关联对象的__str__方法返回的结果
    book_str = serializers.StringRelatedField()

# 针对HeroInfo模型类定义序列化器
class HeroInfoSerializer(serializers.Serializer):
    # 主键隐藏属性
    id = serializers.IntegerField()
    # 固有属性
    hname = serializers.CharField()
    hgender = serializers.IntegerField()
    hcomment = serializers.CharField()
    is_delete = serializers.BooleanField()
    # 关联属性/字段
    # (1)、序列化为关联对象的主键值，read_only=True表明此属性/字段只参与序列化操作
    # hbook = serializers.PrimaryKeyRelatedField(read_only=True)
    # (2)、序列化为关联对象的__str__方法返回的结果
    # hbook = serializers.StringRelatedField()
    # (3)、使用自定义的关联对象模型类序列化器进行序列化
    # hbook = BookInfoSerializer()