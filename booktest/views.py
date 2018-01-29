#coding=utf-8

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Max,F,Q
from .models import *

def index(request):
    # list=BookInfo.books1.filter(heroinfo__hcontent__contains='六')
    # list=BookInfo.books1.filter(pk__lte=3)
    # Max1=BookInfo.books1.aggregate(Max('bpub_date'))
    # list=BookInfo.books1.filter(bread__gt=F('bcommet'))
    # list=BookInfo.books1.filter(pk__lt=4,btitle__contains='1')
    # list=BookInfo.books1.filter(pk__lt=4).filter(btitle__contains='1')
    # list = BookInfo.books1.filter(Q(pk__lt=4) | Q(btitle__contains='1'))
    # context = {'list1': list
    #            # ,'Max1':Max1
    #            }
    bookList = BookInfo.objects.all()
    context = {'list':bookList}
    return render(request, 'booktest/index.html',context)

def show(request, id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list':herolist}
    return render(request, 'booktest/show.html',context)


def detail(request,p1,p2,p3):
    return HttpResponse('year:%s,month:%s,day:%s'%(p1,p2,p3))

#展示链接的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

#接收一键一值的情况
def getTest2(request):
    #根据键接收值
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    #构造上下文
    context={'a':a1,'b':b1,'c':c1}
    #向模板中传递上下文，并进行渲染
    return render(request,'booktest/getTest2.html',context)

#接收一键多值的情况
def getTest3(request):
    a1=request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)

def postTest1(request):
    return render(request,'booktest/postTest1.html')
def postTest2(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST.get('ugender')
    uhobby=request.POST.getlist('uhobby')
    context={'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)

#cookie练习
def cookieTest(request):
    response = HttpResponse()
    cookie=request.COOKIES
    if 't1' in cookie:
        response.write(cookie['t1'])
    # response.set_cookie('t1','abc')
    return response

#转向练习
def redTest1(request):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse('这是转向来的页面')

#通过用户登录练习session
def session1(request):
    uname=request.session.get('myname','未登录')
    context={'uname':uname}
    return render(request,'booktest/session1.html',context)
def session2(request):
    return render(request,'booktest/session2.html')
def session2_handle(request):
    uname=request.POST['uname']
    request.session['myname']=uname
    request.session.set_expiry(0)
    return redirect('/booktest/session1/')
def session3(request):
    #删除session
    del request.session['myname']
    return redirect('/booktest/session1/')