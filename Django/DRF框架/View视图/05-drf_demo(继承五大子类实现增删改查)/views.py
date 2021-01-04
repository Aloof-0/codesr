

# 五大子类
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .serializers import *


class BooksAPIView(ListAPIView, CreateAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer

class BookAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoModelSerializer














