from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import *
urlpatterns=[path('',PostListView.as_view(),name='blog_home'),
             path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'), # As postdetailview is to open a specific post we provide primary key in the url which post to be opened and we can limit entering primarykey datatype to int as here. If we want to use other variables in place of pk we have to specify in the postdetailview class in views.py
             #path('',views.home,name="blog_home"),
             path('post/new/',PostCreateView.as_view(),name='post_create'),
             path('post/<int:pk>/update',PostUpdateView.as_view(),name='post_update'), # As postdetailview is to open a specific post we provide primary key in the url which post to be opened and we can limit entering primarykey datatype to int as here. If we want to use other variables in place of pk we have to specify in the postdetailview class in views.py
            path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post_delete'),
             #path('home',views.home,name="blog_home"),
             path('about',views.about,name="blog_about"),
             path('profile',views.profile,name="profile"),
             #path('addpost',views.addpost,name='addpost'),
              
]

