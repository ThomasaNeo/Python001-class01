from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse

# 从models取数据传给template
from .models import Name


def index(request):
    return HttpResponse("Hello Django!")


def name(request, **kwargs):
    return HttpResponse(kwargs['name'])


def books(request):
    # 从models取数据传给template
    n = Name.objects.all()
    return render(request, 'bookslist.html', locals())


from .form import LoginForm
from django.contrib.auth import authenticate, login


def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')

    # GET
    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'form2.html', {'form': login_form})
