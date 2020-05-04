# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    author = models.ForeignKey(User, related_name='posts',
                               on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=200)
    content = models.TextField(_('Content'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class Comment(TimeStampedModel):
    author = models.ForeignKey(User, related_name='comments',
                               on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField(_('Comment'))

    def __str__(self):
        return truncatechars(self.comment, 30)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


class CommentAttribute(TimeStampedModel):
    comment = models.OneToOneField(Comment, related_name='comment_attribute',
                                   on_delete=models.CASCADE)
    is_bookmark = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.comment

    class Meta:
        verbose_name = _('Comment Attribute')
        verbose_name_plural = _('Comments Attribute')


class PostComment(TimeStampedModel):
    post = models.ForeignKey(Post, related_name='post_comments',
                             on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return '%s' % self.post

    class Meta:
        verbose_name = _('Post Comment')
        verbose_name_plural = _('Post Comments')
