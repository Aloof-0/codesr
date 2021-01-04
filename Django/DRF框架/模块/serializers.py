# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/4 19:33
@Auth ： 高冷Aloof
@File ：serializers.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

# -*- coding: utf-8 -*-
"""
@Time ： 2021/1/3 15:08
@Auth ： 高冷Aloof
@File ：serializer.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from rest_framework import serializers

from .models import BookInfo, HeroInfo


# 模型类序列化器`ModelSerializer`


class BookInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo  # 声明当前序列化器操作的目标模型类

        # 1. fields声明当前序列化器操作目标模型类的字段   __all__表示自动映射所有显示定义的模型类字段和主键隐藏字段
        fields = "__all__"

        # 3.  指定字段映射
        # fields = ['btitle', 'bpub_date']  指定 btitle 和 bpub_date

        # 4. 除了该列表里面的字段以外，其他的字段映射过来
        # exclude = ['is_delete'] 除了is_delete

        # 5. 在该列表里面的字段只参与序列化
        # read_only_fields = ['btitle']

        # 通过extra_kwargs属性来修改默认映射的字段约束条件
        extra_kwargs = {
            'bread': {'min_value': 0},
            'bcomment': {'min_value': 0}
        }


class HeroInfoModelSerializer(serializers.ModelSerializer):
    hbook = BookInfoModelSerializer()  # 重写类属性会覆盖原有的自动映射

    class Meta:
        model = HeroInfo
        fields = "__all__"
