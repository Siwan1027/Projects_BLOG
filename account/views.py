# account/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.http import HttpResponseBadRequest
# 로그인 시 아이디, 비밀번호 인증 폼
from django.contrib.auth.forms import AuthenticationForm
# 로그인, 로그아웃, get_user 메소드
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

User = get_user_model()

# 로그인
@ require_http_methods(['GET', 'POST'])
def signin(request):
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        return redirect(request.GET.get('next') or 'board:index')
    else :
        form = AuthenticationForm()
    return render(request, 'account/singin.html', {
        'form' : form
    })

# 회원가입
@ require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board:index')
    else:
        form = CustomUserCreationForm()
        return render(request, 'account/signup.html', {
            'form' : form
        })
    

def logout(request):
    logout(request)
    return redirect('board:index')



    # path('signin/', views.signin, name = 'signin'),
    # path('signup/', views.signup, name = 'signup'),
    # path('logout/', views.logout, name = 'logout'),