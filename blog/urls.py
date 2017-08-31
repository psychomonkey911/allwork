from django.conf.urls import url
from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^search/$', views.search, name='search'),
]