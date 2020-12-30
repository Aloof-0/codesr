# <font color="orange">   </font><font color="orange">迁移用户模型类并设置域名</font>

### <font color="blue">迁移用户模型类   </font>

##### 创建迁移文件

```python
# 生成迁移文件: 
python manage.py makemigrations
```

效果如图: 

<img src="/user-register/images/122.png" style="zoom:50%">

##### 进行迁移

```python
# 进行数据迁移: 
python manage.py migrate
```

效果如图: 

<img src="/user-register/images/123.png" style="zoom:50%">




### <font color="blue">总结:    </font>

* 如果第二次, 或是第三次进行数据迁移, 生成迁移文件时, 没有执行,  那就把以前的迁移文件删除后, 再生成,  有时候,  django 检测到你有迁移文件时, 它不会再次生成新的. 
* 这两个命令必须背下来,  以后做 django 开发, 100% 用.




