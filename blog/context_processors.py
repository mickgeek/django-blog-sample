# -*- coding: utf-8 -*-

from django.utils import timezone

from .models import Tag, Post


def post_tags(request):
    """
    Returns a context variable that use for rendering the tag menu.
    """
    statuses = [Post.STATUS_PUBLISHED, Post.STATUS_ARCHIVED]
    return {
        'post_tags': Tag.objects.filter(post__status__in=statuses).distinct(),
    }
