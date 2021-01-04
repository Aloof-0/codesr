from book.serializer import *
# Create your views here.
import logging

from book.serializer import *
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView

logger = logging.getLogger('django')


class BookAPIView(APIView):

    # 获取全部数据 序列化查询
    def get(self, request):
        # 获取模型类对象
        book = BookInfo.objects.all()
        # 获取序列器对象
        serializer = BookInfoModelSerializer(instance=book, many=True)  # many - 操作的对象数据是单个还是多个 # instance  是要被赋值对象的
        # 返回数据
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)

    # 新键单一数据 反序列化新键
    def post(self, request):
        # 获取前端数据
        data = request.data  # json格式或表单请求体
        # 获取序列器对象
        serializer = BookInfoModelSerializer(data=data)  # 是要被赋值的对象或数据的-- 请求来的数据给data
        # 判断约束条件
        if not serializer.is_valid():  # .is_valid()返回的是True或False
            logging.error(serializer.errors)
            return Response(data=serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
        # 保存/新建
        serializer.save()
        return Response(data=data, status=status.HTTP_201_CREATED)  # 成功则返回数据


class BookAPIView2(APIView):

    # 获取一条数据 序列化单一查询
    def get(self, request, pk):  # 请求参数:路径中的主键值
        # 获取单一模型类对象
        book = BookInfo.objects.get(pk=pk)
        # 获取序列化器对象
        serializer = BookInfoModelSerializer(instance=book)
        # 返回数据
        data = serializer.data
        return Response(data=data, status=status.HTTP_200_OK)

    # 更新一条数据 反序列化单一更新 必要校验
    def post(self, request, pk):
        # 获取前端数据
        data = request.data
        # 获取单一模型类对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            print(e)
            logging.warning(e)
            return Response(data=None, status=status.HTTP_401_UNAUTHORIZED)
        # 获取序列化器对象
        serializer = BookInfoModelSerializer(instance=book, data=data)
        # 判断数据
        if not serializer.is_valid():
            return Response(data=None, status=status.HTTP_401_UNAUTHORIZED)
        # 保存/新键
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # 更新部分数据 反序列部分更新 部分校验
    def patch(self, request, pk):
        # 获取前端数据
        data = request.data
        # 获取单一模型类对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            print(e)
            logging.warning(e)
            return Response(data=None, status=status.HTTP_401_UNAUTHORIZED)
        # 获取序列化器对象
        serializer = BookInfoModelSerializer(instance=book, data=data, partial=False)  # 在修改需求时,可以将所有校验字段设置为False
        # 判断数据
        if not serializer.is_valid():
            return Response(data=None, status=status.HTTP_401_UNAUTHORIZED)
        # 保存/新键
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    # 删除一条数据
    def delete(self, request, pk):
        # 获取模型类对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except Exception as e:
            logging.warning(e)
            return Response(data=None, status=status.HTTP_401_UNAUTHORIZED)
        # 删除数据
        book.delete()
        return Response(data=None, status=status.HTTP_200_OK)