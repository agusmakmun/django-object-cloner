# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from app.models import (Post, Comment, CommentAttribute, PostComment)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    search_fields = ('id', 'title', 'content')
    raw_id_fields = ('author',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'post', 'author', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    search_fields = ('id', 'comment', 'post__title')
    raw_id_fields = ('author', 'post')


class CommentAttributeAdmin(admin.ModelAdmin):
    list_display = ('comment', 'is_bookmark', 'created_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    search_fields = ('id', 'comment__comment')
    raw_id_fields = ('comment',)


class PostCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'created_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')
    search_fields = ('id', 'post__title')
    raw_id_fields = ('post', 'comments')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentAttribute, CommentAttributeAdmin)
admin.site.register(PostComment, PostCommentAdmin)
