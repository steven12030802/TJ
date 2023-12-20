from django.shortcuts import render

from tjweb.models import *
from tjweb.utils.pv import total_views_add, get_user_ip


# Create your views here.
def index(request):
    gg = Article.objects.all()
    pv = total_views_add()
    req = RotationImg.objects.all()
    xct = AnnounceImg.objects.all()
    return render(request, 'index.html', {'gg': gg, 'pv': pv, 'req': req, 'xct': xct})


def post_view(request, nid):
    req = Article.objects.get(id=nid)
    return render(request, 'post_view.html', {'req': req})


def announce_view(request):
    req = Article.objects.get(belong=1)
    return render(request, 'announce_view.html', {'req': req})
