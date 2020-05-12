# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import truncatechars

User = get_user_model()


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE,
                               null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(TimeStampedModel):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=200)
    price = models.FloatField(_('Price'))
    stock = models.PositiveIntegerField(_('Stock'), default=1)
    description = models.TextField(_('Description'))
    categories = models.ManyToManyField(Category, related_name='categories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductInfo(TimeStampedModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    note = models.TextField(_('Note'), null=True, blank=True)
    location = models.TextField(_('Location'), null=True, blank=True)

    def __str__(self):
        return '%s' % self.product

    class Meta:
        verbose_name = _('Product Info')
        verbose_name_plural = _('Product Infos')


class ProductSKU(TimeStampedModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku_id = models.CharField(_('SKU ID'), max_length=200)

    def __str__(self):
        return '%s' % self.product

    class Meta:
        verbose_name = _('Product SKU')
        verbose_name_plural = _('Product SKU')


class ProductImages(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='product_images')
    image_url = models.TextField(_('Image URL'))
    caption = models.CharField(_('Caption'), max_length=200, null=True, blank=True)

    def __str__(self):
        if self.caption:
            return self.caption
        return truncatechars(self.image_url, 50)

    class Meta:
        verbose_name = _('Product Images')
        verbose_name_plural = _('Product Images')
