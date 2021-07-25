

from rest_framework import status
# Response是drf中唯一的响应对象
from rest_framework.response import Response
from rest_framework.views import APIView


# 编写一个测试接口，研究APIView的请求对象如何提取参数
# 前端传参数形式：1、路径参数；2、查询字符串参数；3、请求体(表单或json)；4、请求头

# 接口定义
# POST + /test/1/?name=weiwei&age=18
class IndexView(APIView):
    # (1)、APIView的路由分发原理是继承自django的View的
    # (2)、路径参数的提取仍然和Django原生提取方式一样
    # (3)、APIView视图中的请求对象是DRF框架对Django请求对象的二次封装(支持Django请求对象的使用)
    # (4)、通过request.query_params(类型为QueryDict)提取查询字符串参数
    # (5)、通过request.data提取请求体参数(json参数封装成普通字典类型，表单参数封装成QueryDict类型)

    def post(se lf, request, pk):

        # /test/1/?name=weiwei&age=18&age=28
        # 1、通过请求对象提取查询字符串参数 -->  对应django的request.GET提取查询字符串参数
        # query_params是一个QueryDict类型。
        # print('request.query_params的类型: ', type(request.query_params))
        # name = request.query_params.get('name')
        # print("name: ", name)
        # age = request.query_params.get('age')
        # print("age: ", age)
        # print("所有的age: ", request.query_params.getlist('age'))

        # 2、通过请求对象提取请求体参数  -->  对应django的request.body提取请求体参数；json需要手动转化，表单被自动提取封装成了request.POST
        # 根据请求头`Content-Type: application/json`; json格式请求体数据，自动提取，封装到了request.data中，是一个普通字典类型
        # 根据请求头`Content-Type: application/x-www-form-urlencoded`; 表单格式请求体数据，自动提取，封装改了request.data中，是一个QueryDict类型
        # print("请求体参数：", request.data)

        # 3、请求头参数提取
        # META属性中，请求头中的key全部是大写
        # print("请求头参数：", request.META)
        # print("请求体参数类型：", request.META.get('CONTENT_TYPE'))
        # headers属性中，请求头中的key全部都是原来的，没有做任何改变
        # print(request.headers)
        # print("请求体类型：", request.headers.get('Content-Type'))

        # DRF响应对象
        return Response(
            data={'name':'weiwei', 'age': 18}, # 字典或列表嵌套字典,将来会默认被序列化成json返回
            status=status.HTTP_200_OK,
            headers={'server-version': '1.0'},
            # content_type='application/json' # drf默认响应体就是json格式
        )















