from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Type(models.Model):
    name = models.CharField(verbose_name="名称", max_length=256)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "类型管理"
        verbose_name_plural = "类型管理"


class Article(models.Model):
    title = models.CharField(verbose_name="文章标题", max_length=256)
    belong = models.ForeignKey(to=Type, verbose_name="所属类型", on_delete=models.CASCADE)
    content = models.FileField(verbose_name="正文文件", upload_to='data')
    create_date = models.DateTimeField(verbose_name="创建日期", auto_now_add=True)
    create_user = models.ForeignKey(to=User, verbose_name="创建人", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "文章管理"
        verbose_name_plural = "文章管理"


# 首页轮播图
class RotationImg(models.Model):
    name = models.CharField(verbose_name="轮播图名称", max_length=128)
    img = models.ImageField(verbose_name="图片文件", upload_to="rotationimg")
    aid = models.ForeignKey(to=Article, verbose_name="跳转文章ID", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "轮播图管理"
        verbose_name_plural = "轮播图管理"


# 宣传图
class AnnounceImg(models.Model):
    name = models.CharField(verbose_name="名称", max_length=128)
    img = models.ImageField(verbose_name="宣传图文件", upload_to="announceimg")
    aid = models.ForeignKey(to=Article, verbose_name="跳转文章ID", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "宣传图管理"
        verbose_name_plural = "宣传图管理"


class WebsiteViews(models.Model):
    """
    网站访问量统计表：字段ID、总访问量
    """
    nid = models.AutoField(primary_key=True)
    views = models.IntegerField()

    def __str__(self):
        return str(self.nid)

    class Meta:
        verbose_name = "访问量统计"
        verbose_name_plural = "访问量统计"


class ViewIp(models.Model):
    """
    最近访问用户IP：字段ID、用户IP
    """
    nid = models.AutoField(primary_key=True)
    user_ip = models.CharField(max_length=15, null=False)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user_ip)

    class Meta:
        verbose_name = "访客统计"
        verbose_name_plural = "访客统计"

