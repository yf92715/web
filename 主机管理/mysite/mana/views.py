from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from mana import models


TEMP_ID = ''
HOST_LIST = []


def register(request):
    error_msg = ''
    if request.method == 'POST':
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        result = models.UserInfo.objects.filter(username=user)
        if result:
            error_msg = '用户已存在，请重新创建'
        else:
            models.UserInfo.objects.create(username=user, password=pwd)
            return redirect('/enter')
    return render(request, 'register.html', {'error_msg': error_msg})


def handle(request):
    global HOST_LIST
    if request.method == 'POST':
        hostname_ = request.POST.get('hostname', None)
        task_ = request.POST.get('task', None)
        user_id = TEMP_ID
        models.HostInfo.objects.create(hostname=hostname_, task=task_, user_info_id=user_id)
    HOST_LIST = models.HostInfo.objects.filter(user_info_id=TEMP_ID)
    host_list = HOST_LIST
    return render(request, 'handle.html', {'host_list': host_list})


def host_del(request, uid):
    models.HostInfo.objects.filter(id=uid).delete()
    return redirect('/handle')


def edit(request, uid):
    if request.method == 'POST':
        hostname_ = request.POST.get('hostname', None)
        task_ = request.POST.get('task', None)
        user_id = TEMP_ID
        models.HostInfo.objects.filter(id=uid).update(hostname=hostname_, task=task_, user_info_id=user_id)
    return redirect('/handle')


def host_detail(request, uid):
    host = models.HostInfo.objects.filter(id=uid).first()
    return render(request, 'detail.html', {'host':host})

def enter(request):
    # 包含了用户的所有信息
    global TEMP_ID
    global HOST_LIST
    error_msg = ''
    if request.method == 'POST':
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        result = models.UserInfo.objects.filter(username=user)
        if result:
            TEMP_ID = result[0].id
            HOST_LIST = models.HostInfo.objects.filter(user_info_id=TEMP_ID)
            if result[0].password == pwd:
                return redirect('/handle')
            else:
                error_msg = '用户名或密码错误'
        else:
            error_msg = '用户名或密码错误'
    return render(request, 'enter.html', {'error_msg':error_msg})


# def detail(request, nid):
#     user_info = USER_DICT[nid]
#     return render(request, 'detail.html', {'id': nid, '用户信息': user_info})
