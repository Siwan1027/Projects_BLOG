#  account/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,  get_user_model
# 로그인 시 아이디, 비밀번호 인증 폼
from django.contrib.auth.forms import AuthenticationForm
# 로그인, 로그아웃, get_user 메소드
from django.contrib.auth import login, logout, get_user_model
from .forms import CustomUserCreationForm


User = get_user_model()
# Create your views here.

def signin(request):
    if request.user.is_authenticated:
        return redirect('board:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, request.POST)
        # 4.9 19:39
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board:index')
    else:
        form = CustomUserCreationForm()
        return render(request, 'account/signup.html', context={
            'form' : form
        })
def logout(request):
    pass



    # path('signin/', views.signin, name = 'signin'),
    # path('signup/', views.signup, name = 'signup'),
    # path('logout/', views.logout, name = 'logout'),