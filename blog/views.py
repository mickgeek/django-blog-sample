# -*- coding: utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.utils import dateformat

from .models import Post, Tag


class PostListView(ListView):
    queryset = Post.objects.published()
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostListByTagView(ListView):
    context_object_name = 'posts'
    allow_empty = False
    template_name_suffix = '_list_by_tag'

    def get_queryset(self):
        return Post.objects.active().filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(PostListByTagView, self).get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context


def post_archive(request):
    posts = Post.objects.active()
    years = {}
    for post in posts:
        year = dateformat.format(post.published_date, 'Y')
        if year not in years:
            years[year] = [post]
        else:
            years[year].append(post)
    return render(request, 'blog/post_archive.html', {'years': years})
