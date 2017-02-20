#! -*- coding: utf-8 -*-

from django.conf.urls import url

from blog.views import PostsListView, PostDetailView, about_page

urlpatterns = [
    url(r'^$', PostsListView.as_view(), name='list'),   # http://имя_сайта/
    url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),   # http://имя_сайта/N/
    url(r'^about/$', about_page),   # http://имя_сайта/about/
]
