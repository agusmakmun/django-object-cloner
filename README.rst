django-object-cloner
====================

Easy way to clone/duplicate the objects including their child's with recursively.


    For real case in e-commerce system like amazon, e-bay, etc. When you become a seller and you have the products to sale,
    one of the feature in seller admin such is "duplicate product/copy product/clone product"
    to make the seller easy clone/duplicate the similar product without uploading again.


Strategy
-----------------

1. ``def clone_object(obj, attrs={})`` starts by build a "flat" clone of the given "obj"
2. M2M fields are managed by replicating all related records found on parent "obj" into "clone"
3. for 1-1 and 1-N relations, we clone all child objects by calling recursively ``clone_object()``, but overridding the remote field with the new cloned object

::

    >>> from object_cloner.utils import clone_object
    >>> from app.models import Product
    >>>
    >>> product = Product.objects.first()
    >>> product.pk
    1
    >>>
    >>> cloned_product = clone_object(product)
    >>> cloned_product.pk
    2
    >>>



Proudly thanks to @morlandi who solved this problem (https://stackoverflow.com/a/61729857/6396981)
