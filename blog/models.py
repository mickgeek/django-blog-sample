# -*- coding: utf-8 -*-

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PostQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status__in=[Post.STATUS_PUBLISHED, Post.STATUS_ARCHIVED])

    def published(self):
        return self.filter(status=Post.STATUS_PUBLISHED)


class Post(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLISHED = 2
    STATUS_ARCHIVED = 3
    STATUSES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_ARCHIVED, 'Archived'),
    )

    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    snippet = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True)
    status = models.SmallIntegerField(choices=STATUSES)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
