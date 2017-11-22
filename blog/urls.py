# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views
from .views import PostListView, PostDetailView, PostListByTagView

urlpatterns = [
    url(r'^(page(?P<page>\d+)/)?$', PostListView.as_view(), name='post-list'),
    url(r'^tags/(?P<slug>[-\w]+)/(page(?P<page>\d+)/)?$',
        PostListByTagView.as_view(), name='post-list-by-tag'),
    url(r'^archive/$', views.post_archive, name='post-archive'),
    url(r'^(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post-detail'),
]
