from notifications.signals import notify
# 发送消息
notify.send(user,recipient=users, verb="消息内容")

# 获取消息类
Notification.objects.all() 获取所有的消息类

# 实例
for i in user_list:
    user = User.objects.get(Q(id=i) & Q(is_active=True))
    if request.user.id == i:
        notify.send(request.user, recipient=request.user, verb="添加了{}部门成功".format(g_name))
    notify.send(request.user, recipient=user, verb="管理员 {} 拉您进入了 {}".format(request.user, g_name))