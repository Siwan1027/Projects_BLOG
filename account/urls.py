# account/urls.py
from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signin/', views.signin, name = 'signin'),
    path('signup/', views.signup, name = 'signup'),
    path('signout/', views.signout, name = 'signout'),
    path('<str:username>', views.profile, name = 'profile'),
    path('<str:username>/follow', views.follow, name = 'follow'),
]
