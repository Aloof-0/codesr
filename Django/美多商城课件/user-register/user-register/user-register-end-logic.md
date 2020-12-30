# <font color="orange">用户注册后端逻辑   </font>

> 在 users.views.py 中添加如下代码

```python
class RegisterView(View):

    def post(self, request):
        '''接收参数, 保存到数据库'''
        # 1.接收参数
        dict = json.loads(request.body.decode())
        username = dict.get('username')
        password = dict.get('password')
        password2 = dict.get('password2')
        mobile = dict.get('mobile')
        allow = dict.get('allow')
        sms_code_client = dict.get('sms_code')

        # 2.校验(整体)
        if not all([username, password, password2, mobile, allow, sms_code_client]):
            return http.JsonResponse({'code':400,
                                      'errmsg':'缺少必传参数'})

        # 3.username检验
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return http.JsonResponse({'code': 400,
                                      'errmsg': 'username格式有误'})

        # 4.password检验
        if not re.match(r'^[a-zA-Z0-9]{8,20}$', password):
            return http.JsonResponse({'code': 400,
                                      'errmsg': 'password格式有误'})

        # 5.password2 和 password
        if password != password2:
            return http.JsonResponse({'code': 400,
                                      'errmsg': '两次输入不对'})
        # 6.mobile检验
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return http.JsonResponse({'code': 400,
                                      'errmsg': 'mobile格式有误'})
        # 7.allow检验
        if allow != True:
            return http.JsonResponse({'code': 400,
                                      'errmsg': 'allow格式有误'})

        # 8.sms_code检验 (链接redis数据库)
        redis_conn = get_redis_connection('verify_code')

        # 9.从redis中取值
        sms_code_server = redis_conn.get('sms_%s' % mobile)

        # 10.判断该值是否存在
        if not sms_code_server:
            return http.JsonResponse({'code': 400,
                                      'errmsg': '短信验证码过期'})
        # 11.把redis中取得值和前端发的值对比
        if sms_code_client != sms_code_server.decode():
            return http.JsonResponse({'code': 400,
                                      'errmsg': '验证码有误'})

        # 12.保存到数据库 (username password mobile)
        try:
            user =  User.objects.create_user(username=username,
                                     password=password,
                                     mobile=mobile)
        except Exception as e:
            return http.JsonResponse({'code': 400,
                                      'errmsg': '保存到数据库出错'})

        # 13.拼接json返回
        return http.JsonResponse({'code': 0,
                                 'errmsg': 'ok'})

```



### <font color="blue">响应注册结果   </font>

> **1.创建首页广告应用：contents**
>
> 在 contents.views.py 中添加如下代码

```bash
$ cd ~/projects/meiduo_project/meiduo_mall/meiduo_mall/apps
$ python ../../manage.py startapp contents
```

<img src="/user-register/images/11广告首页应用.png" style="zoom:50%">















### <font color="blue">总结: </font>

1. 后端逻辑编写套路：
    * 业务逻辑分析
    * 接口设计和定义
    * 接收参数
    * 校验参数
    * 实现主体业务逻辑
    * 响应结果
2. 注册主体业务逻辑核心部分：
    * 保存用户注册数据并得到用户实例


