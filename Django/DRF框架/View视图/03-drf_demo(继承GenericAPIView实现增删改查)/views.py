from rest_framework import status
# GenericAPIView通用视图类(核心类)
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .serializers import *


class BooksAPIView(GenericAPIView):
    # 通过类属性queryset指定当前视图处理的默认查询集 —— 也是self.get_queryset()默认返回值
    queryset = BookInfo.objects.all()
    # 通过类属性serializer_class指定当前视图处理数据默认使用的序列化器(类) —— self.get_serializer()返回的就是该序列化器的实例化对象
    serializer_class = BookInfoModelSerializer

    # 获取列表数据
    # GET + /books/
    def get(self, request):
        # 1、获取目标数据 —— 多个模型类对象查询集
        books = self.get_queryset()  # 要么重写该方法返回查询集，要么设置cls.queryset类属性指定默认查询集

        # 2、实例化序列化器对象
        # serializer = BookInfoModelSerializer(instance=books, many=True)
        serializer = self.get_serializer(instance=books, many=True)  # 要么重写该方法返回序列化器对象，要么设置cls.serializer_class类属性指明序列化器

        # 3、获取序列化的结果: serializer.data
        # 4、构建响应
        return Response(data=serializer.data)

    # 新建单一数据
    # POST + /books/
    def post(self, request):
        # 1、获取前端参数: request.data
        # 2、实例化序列化器对象
        serializer = self.get_serializer(data=request.data)
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


class BookAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

    # 过滤的依据字段为pk，lookup_field默认值就是pk
    # lookup_field = 'pk' # 相当于过滤的时候BookInfo.objects.get(pk=???)
    # 路由提取的前端传值主键值使用的关键字, lookup_url_kwarg默认值等于lookup_field
    # lookup_url_kwarg = 'pk' # books/<int:pk>/

    # 获取一条数据
    # GET+ /books/<pk>/
    def get(self, request, pk):
        # 1、获取目标数据
        # 获取单一目标模型类对象
        # 需要的已知条件有哪些？
        # (1)、从哪个查询集中过滤出唯一的对象；
        # (2)、指定唯一过滤的字段(主键字段pk或id或自定义主键字段) --> BookInfo.objects.get(pk=???)
        # (3)、路由提取的前端传递主键值使用的关键字
        book = self.get_object()

        # 2、实例化序列化器对象

        serializer = self.get_serializer(instance=book)

        # 3、获取序列化的结果：serializer.data
        # 4、构建响应
        return Response(serializer.data)

    # 全更新一条 数据
    # PUT + /books/<pk>/
    def put(self, request, pk):
        # 1、获取目标数据 —— 被更新的单一模型类对象
        book = self.get_object()
        # 2、获取前端参数：request.data
        # 3、获取序列化器对象
        serializer = self.get_serializer(instance=book, data=request.data)
        # 4、启动校验步骤
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 5、更新
        serializer.save()
        # 6、构建响应
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 部分更新一条数据
    # PATCH + /books/<pk>/
    def patch(self, request, pk):
        # 1、获取目标数据 ——被更新的模型类对象
        book = self.get_object()
        # 2、获取前端参数：request.data
        # 3、获取序列化器对象
        serializer = self.get_serializer(instance=book, data=request.data, partial=True)
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
        book = self.get_object()
        # 2、直接删除
        book.delete()
        # 3、构建响应返回(响应体无数据)
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
