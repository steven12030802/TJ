from django.shortcuts import render

from tjweb.models import *
from tjweb.utils.pv import total_views_add


# Create your views here.
def index(request):
    # 公告
    gg = Article.objects.filter(belong=1)
    # 浏览量
    pv = total_views_add()
    # 轮播图
    req = RotationImg.objects.all()
    # 宣传图
    xct = AnnounceImg.objects.all()
    # 友链
    jump = Jump.objects.all()
    # 工作动态
    work_list = Article.objects.filter(belong=2)
    return render(request, 'index.html',
                  {'gg': gg, 'pv': pv, 'req': req, 'xct': xct, 'jump': jump, 'work_list': work_list})


def post_view(request, nid):
    req = Article.objects.get(id=nid)
    return render(request, 'post_view.html', {'req': req})


def announce_view(request):
    req = Article.objects.filter(belong=1)
    return render(request, 'announce_view.html', {'req': req})


def work_view(request):
    req = Article.objects.filter(belong=2)
    return render(request, 'work_view.html', {'req': req})


def department_view(request):
    req = Article.objects.filter(belong=3)
    return render(request, 'department_view.html', {'req': req})


def check_view(request):
    req = Article.objects.filter(belong=4)
    return render(request, 'check_view.html', {'req': req})


def project_view(request):
    req = Article.objects.filter(belong=5)
    return render(request, 'project_view.html', {'req': req})
