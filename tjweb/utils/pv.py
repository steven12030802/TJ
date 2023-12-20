from datetime import datetime

from tjweb import models


def get_user_ip(request):
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # 获取用户真实IP地址
        user_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        user_ip = request.META['REMOTE_ADDR']
    obj = models.ViewIp.objects.first()
    if obj is not None:  # 判断数据表是否为空
        ct = obj.create_time
        if not ct.month == datetime.now().month or not ct.day == datetime.now().day:  # 判断表中数据是否为当日访问
            objs = models.ViewIp.objects.all()  # 不是当日访问则迭代删除表中数据
            for i in objs:
                i.delete()
        if not models.ViewIp.objects.filter(user_ip=user_ip):  # 判断当日用户是否已经访问过本网站
            models.ViewIp.objects.create(user_ip=user_ip)  # 将用户IP存入数据库
            total_views_add()  # 网站总访问量+1
    else:
        print(user_ip)
        models.ViewIp.objects.create(user_ip=user_ip)
        total_views_add()


def total_views_add():
    obj = models.WebsiteViews.objects.first()
    if obj is None:
        models.WebsiteViews.objects.create(views=1)
    else:
        total_views = models.WebsiteViews.objects.first()
        total_views.views = total_views.views + 1
        total_views.save()
