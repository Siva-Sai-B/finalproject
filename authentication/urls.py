from django.contrib import admin
from django.urls import path,re_path
from django.views import static
from django.views.static import serve
from loginsystem import settings
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('results',views.results,name="view_results"),
    path('sem1',views.sem1,name="view_results"),
    path('sem2',views.sem2,name="view_results"),
    path('sem3',views.sem1,name="view_results"),
    path('sem4',views.sem1,name="view_results"),
    path('sem5',views.sem1,name="view_results"),
    path('sem6',views.sem1,name="view_results"),
    path('gvp',views.gvp,name="About GVP"),
    path('activate/<uidb64>/<token>',views.activate,name="activate"),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT})
]
