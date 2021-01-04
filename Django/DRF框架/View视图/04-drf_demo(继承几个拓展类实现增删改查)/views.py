# GenericAPIView通用视图类(核心类)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin

from .serializers import *


class BooksAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    # 通过类属性queryset指定当前视图处理的默认查询集 —— 也是self.get_queryset()默认返回值
    queryset = BookInfo.objects.all()
    # 通过类属性serializer_class指定当前视图处理数据默认使用的序列化器(类) —— self.get_serializer()返回的就是该序列化器的实例化对象
    serializer_class = BookInfoModelSerializer

    # 获取列表数据
    # GET + /books/
    def get(self, request):
        return self.list(request)

    # 新建单一数据
    # POST + /books/
    def post(self, request):
        return self.create(request)


class BookAPIView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer


    # 获取一条数据
    # GET+ /books/<pk>/
    def get(self, request, pk):
        return self.retrieve(request, pk)

    # 全更新一条数据
    # PUT + /books/<pk>/
    def put(self, request, pk):
        return self.update(request, pk)

    # 部分更新一条数据
    # PATCH + /books/<pk>/
    def patch(self, request, pk):
        return self.partial_update(request, pk)

    # 删除一条数据
    # DELETE + /books/<pk>/
    def delete(self, request, pk):
        return self.destroy(request, pk)














