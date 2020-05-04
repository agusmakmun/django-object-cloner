# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.utils import IntegrityError


class ObjectCloner(object):
    """
    [1]. The simple way with global configuration:
    >>> cloner = ObjectCloner()
    >>> cloner.set_objects = [obj1, obj2]   # or can be queryset
    >>> cloner.include_childs = True
    >>> cloner.max_clones = 1
    >>> cloner.execute()

    [2]. Clone the objects with custom configuration per-each objects.
    >>> cloner = ObjectCloner()
    >>> cloner.set_objects = [
        {
            'object': obj1,
            'include_childs': True,
            'max_clones': 2
        },
        {
            'object': obj2,
            'include_childs': False,
            'max_clones': 1
        }
    ]
    >>> cloner.execute()
    """
    set_objects = []            # list/queryset of objects to clone.
    include_childs = True       # include all their childs or not.
    max_clones = 1              # maximum clone per-objects.

    def clone_object(self, object):
        """
        function to clone the object.
        :param `object` is an object to clone, e.g: <Post: object(1)>
        :return new object.
        """
        try:
            object.pk = None
            object.save()
            return object
        except IntegrityError:
            return None

    def clone_childs(self, object):
        """
        function to clone all childs of current `object`.
        :param `object` is a cloned parent object, e.g: <Post: object(1)>
        :return
        """
        # bypass the none object.
        if object is None:
            return

        # find the related objects contains with this current object.
        # e.g: (<ManyToOneRel: app.comment>,)
        related_objects = object._meta.related_objects

        if len(related_objects) > 0:
            for relation in related_objects:
                # find the related field name in the child object, e.g: 'post'
                remote_field_name = relation.remote_field.name

                # find all childs who have the same parent.
                # e.g: childs = Comment.objects.filter(post=object)
                childs = relation.related_model.objects.all()

                for old_child in childs:
                    new_child = self.clone_object(old_child)

                    if new_child is not None:
                        # check the object_type
                        object_type = getattr(new_child, remote_field_name)

                        if hasattr(object_type, 'pk'):
                            # this mean is `object_type` as real object.
                            # so, we can directly use the `setattr(...)`
                            # to update the old relation value with new relation value.
                            setattr(new_child, remote_field_name, object)

                        elif hasattr(object_type, '_queryset_class'):
                            # this mean is `object_type` as m2m queryset (ManyRelatedManager).
                            # django.db.models.fields.related_descriptors.\
                            # create_forward_many_to_many_manager.<locals>.ManyRelatedManager

                            # check the old m2m values, and assign into new object.
                            # FIXME: IN THIS CASE STILL GOT AN ERROR
                            old_m2m_values = getattr(old_child, remote_field_name).all()
                            object_type.add(*old_m2m_values)

                        new_child.save()

                    self.clone_childs(new_child)

                # try:
                #     new_child = self.clone_object(old_child)
                #     # setattr(new_child, remote_field_name, object)
                #     # new_child.save()
                #
                #     # FIXME: PROBLEM FOUND HERE,
                #     # WHY THE `id` of `old_child` also same with `new_child`?
                #     # print(old_child.id, new_child.id)
                #     # print(old_child.post_id, new_child.post_id)
                #
                #     return self.clone_childs(new_child)
                # except IntegrityError:
                #     pass

                # return self.clone_childs(object)
        return

    def execute(self):
        include_childs = self.include_childs
        max_clones = self.max_clones
        new_objects = []

        for old_object in self.set_objects:
            # custom per-each objects by using dict {}.
            if isinstance(old_object, dict):
                include_childs = old_object.get('include_childs', True)
                max_clones = old_object.get('max_clones', 1)
                old_object = old_object.get('object')  # assigned as object or None.

            for _ in range(max_clones):
                new_object = self.clone_object(old_object)
                if new_object is not None:
                    if include_childs:
                        self.clone_childs(new_object)
                    new_objects.append(new_object)

        return new_objects
