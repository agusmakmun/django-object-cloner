# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db.models import (ForeignKey, OneToOneField,
                              CharField, TextField)

from app.models import (Category, Product, ProductInfo,
                        ProductSKU, ProductImages)


class DefaultAdminMixin:
    """
    class mixin to setup default `raw_id_fields` and `search_fields`.
    """
    raw_id_fields = ()
    search_fields = ()

    def __init__(self, model, admin_site, *args, **kwargs):
        self.raw_id_fields = self.setup_raw_id_fields(model)
        self.search_fields = self.setup_search_fields(model)
        super().__init__(model, admin_site, *args, **kwargs)

    def setup_raw_id_fields(self, model):
        return tuple(
            f.name
            for f in model._meta.get_fields()
            if isinstance(f, ForeignKey) or isinstance(f, OneToOneField)
        )

    def setup_search_fields(self, model):
        return tuple(
            f.name
            for f in model._meta.get_fields()
            if isinstance(f, CharField) or isinstance(f, TextField)
        )


class CategoryAdmin(DefaultAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'parent', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')


class ProductAdmin(DefaultAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'seller', 'price', 'stock',
                    'created_at', 'updated_at', 'deleted_at')
    list_filter = ('categories', 'created_at', 'updated_at', 'deleted_at')


class ProductInfoAdmin(DefaultAdminMixin, admin.ModelAdmin):
    list_display = ('product', 'note', 'location',
                    'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')


class ProductSKUAdmin(DefaultAdminMixin, admin.ModelAdmin):
    list_display = ('sku_id', 'product', 'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')


class ProductImagesAdmin(DefaultAdminMixin, admin.ModelAdmin):
    list_display = ('__str__',  'author', 'caption',
                    'created_at', 'updated_at', 'deleted_at')
    list_filter = ('created_at', 'updated_at', 'deleted_at')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(ProductSKU, ProductSKUAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
