# -*- coding: utf-8 -*-

from django import forms
from django.utils import timezone
from django.contrib import admin

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Tag


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'created_date', 'updated_date', 'published_date')
        widgets = {
            'body': CKEditorUploadingWidget(),
            'snippet': CKEditorUploadingWidget(config_name='small'),
        }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'published_date', 'author']
    date_hierarchy = 'created_date'
    list_filter = ('created_date', 'status')
    search_fields = ['title']

    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        if (obj.published_date is None
                and obj.status in [Post.STATUS_PUBLISHED, Post.STATUS_ARCHIVED]):
            obj.published_date = timezone.now()
        if change:
            obj.updated_date = timezone.now()
        super(PostAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
