# <font color="orange">展示用户注册界面   </font>

### <font color="blue">准备用户注册模板文件   </font>

<img src="/user-register/images/10准备注册模板文件.png" style="zoom:50%">

### <font color="blue">定义用户注册视图   </font>

```python
class RegisterView(View):
    """用户注册"""

    def get(self, request):
        """
        提供注册界面
        :param request: 请求对象
        :return: 注册界面
        """
        return render(request, 'register.html')
```

### <font color="blue">定义用户注册路由   </font>

> **1.总路由**

```python
urlpatterns = [
    # users
    url(r'^', include('users.urls', namespace='users')),
]
```

> **2.子路由**

```python
urlpatterns = [
    # 注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
]
```

### <font color="blue">   </font>

##### 1. 访问链接, 查看效果 :

> 我们现在可以访问刚刚定义好的接口:  localhost:8000/register/ 

> 可以看到缺少样式的界面:   

<img src="/user-register/images/QQ20.png" style="zoom:50%">

##### 2. 加载样式: 

> 修改 register.html 文件中的 link 标签, 增加样式: 

```html
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<title>美多商城-注册</title>
<!-- 修改下面两行代码, 使样式能够显示出来 -->
	<link rel="stylesheet" type="text/css" href="{{ static('css/reset.css') }}">
	<link rel="stylesheet" type="text/css" href="{{ static('css/main.css') }}">
</head>
```

> 修改上面的代码后, 我们会发现: 

<img src="/user-register/images/QQ21.png" style="zoom:50%">

##### 3. 修改图片路径, 使图片能够正常显示出来:

> 第一处修改的地方: 

```html
<div class="l_con fl">
    <a href="index.html" class="reg_logo">
        <!-- 修改下面的代码, 使 logo 图片能够显示出来 -->
        <img src="{{ static('images/logo.png') }}">
    </a>
    <div class="reg_slogan">商品美 · 种类多 · 欢迎光临</div>
    <div class="reg_banner"></div>
</div>
```

> 第二处修改的地方: 

```html
<li>
    <label>图形验证码:</label>
    <input type="text" name="pic_code" id="pic_code" class="msg_input">
    <!-- 修改下面的代码, 使图片验证码的图片能够显示出来 -->
    <img src="{{ static('images/pic_code.jpg') }}" alt="图形验证码" class="pic_code">
    <span class="error_tip">请填写图形验证码</span>
</li>
```

##### 4. 再次展示样式

>  我们会发现: 样式 和 图片 能够正常展示了.

<img src="/user-register/images/QQ22.png" style="zoom:50%">





### <font color="blue">总结:    </font>

* 我们定义了一个函数, 返回了模板中的页面

* 定义好后, 需要路由才能够访问到, 故需要添加对应路由

* 返回的页面, 可能有样式问题, 所以, 我们修改修改里面的样式部分.

	