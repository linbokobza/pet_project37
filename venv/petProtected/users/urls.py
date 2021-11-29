from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path('home', views.home_page, name="home"),
    path('signup', views.signUp, name="signup"),
    path('signin', views.signIn, name="signin"),
    path('addpost', views.add_post, name="addpost"),
    path('addreview', views.add_review, name="addreview"),
    path('posts', views.posts, name="posts"),
    path('signout', views.signOut, name="signout"),
    path('loginDetails', views.loginDetails, name="loginDetails"),
    path('loginsuccess', views.login_success, name="login success"),
    path('loginfailed', views.login_failed, name="loginfailed"),

]