
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class BooksAPIView(APIView):

    # 获取列表数据
    # GET + /books/
    def get(self, request):
        # 1、获取目标数据 —— 多个模型类对象查询集
        books = BookInfo.objects.all()
        # 2、实例化序列化器对象
        serializer = BookInfoModelSerializer(instance=books, many=True)
        # 3、获取序列化的结果: serializer.data
        # 4、构建响应
        return Response(data=serializer.data)

    # 新建单一数据
    # POST + /books/
    def post(self, request):
        # 1、获取前端参数: request.data
        # 2、实例化序列化器对象
        serializer = BookInfoModelSerializer(data=request.data)
        # 3、启动校验步骤
        if not serializer.is_valid():
            # 如果校验失败
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 4、新建保存数据
        serializer.save()
        # 5、构建响应返回
        # 注意：当我们完成新建，序列化器对象中就有个新建的模型类对象
        # 我们就可以使用data属性进一步获取该新建对象的序列化结果
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookAPIView(APIView):

    # 获取一条数据
    # GET+ /books/<pk>/
    def get(self, request, pk):
        # 1、获取目标数据
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist as e:
            return Response({'errno': 400, 'errmsg': '资源找不到'}, status=status.HTTP_404_NOT_FOUND)
        # 2、实例化序列化器对象
        serializer = BookInfoModelSerializer(instance=book)
        # 3、获取序列化的结果：serializer.data
        # 4、构建响应
        return Response(serializer.data)

    # 全更新一条数据
    # PUT + /books/<pk>/
    def put(self, request, pk):
        # 1、获取目标数据 —— 被更新的单一模型类对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist as e:
            return Response({'errno': 400, 'errmsg': '资源找不到'}, status=status.HTTP_404_NOT_FOUND)
        # 2、获取前端参数：request.data
        # 3、获取序列化器对象
        serializer = BookInfoModelSerializer(instance=book, data=request.data)
        # 4、启动校验步骤
        if not ser0ializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 5、更新
        serializer.save()
        # 6、构建响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 部分更新一条数据
    # PATCH + /books/<pk>/
    def patch(self, request, pk):
        # 1、获取目标数据 ——被更新的模型类对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist as e:
            return Response({'errno': 400, 'errmsg': '资源找不到'}, status=status.HTTP_404_NOT_FOUND)
        # 2、获取前端参数：request.data
        # 3、获取序列化器对象
        serializer = BookInfoModelSerializer(instance=book, data=request.data, partial=True)
        # 4、启动校验步骤
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 5、更新
        serializer.save()
        # 6、构建响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 删除一条数据
    # DELETE + /books/<pk>/
    def delete(self, request, pk):
        # 1、获取目标数据 —— 被删除的模型类对象
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist as e:
            return Response({'errno': 400, 'errmsg': '资源找不到'}, status=status.HTTP_404_NOT_FOUND)
        # 2、直接删除
        book.delete()
        # 3、构建响应返回(响应体无数据)
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)