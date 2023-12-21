from django.contrib import admin

from tjweb.models import *

from tjweb.models import WebsiteViews, ViewIp

# Register your models here.
admin.site.site_header = '甘肃省人民检察院兰铁分院管理后台'  # 设置header
admin.site.site_title = '甘肃省人民检察院兰铁分院管理后台'  # 设置title
admin.site.index_title = '甘肃省人民检察院兰铁分院管理后台'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'belong')


# class TypeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')


class AnnounceImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'aid')


# admin.site.register(Type, TypeAdmin)
@admin.register(RotationImg)
class RotationImgAdmin(admin.ModelAdmin):
    list_display = ('name', 'img', 'aid')


admin.site.register(Article, ArticleAdmin)
admin.site.register(AnnounceImg, AnnounceImgAdmin)


@admin.register(Jump)
class JumpAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title', 'url')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('logo', 'title', 'url')


@admin.register(WebsiteViews)
class ViewIpAdmin(admin.ModelAdmin):
    list_display = ('nid', 'views')


@admin.register(ViewIp)
class ViewIpAdmin(admin.ModelAdmin):
    list_display = ('nid', 'user_ip', 'create_time')
