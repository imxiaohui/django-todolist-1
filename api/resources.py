from django.contrib.auth.models import User

from tastypie.resources import ModelResource
from tastypie import fields

from lists.models import TodoList, Todo


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        excludes = ['email', 'password', 'is_superuser']
        allowed_methods = ['get']


class TodoListResource(ModelResource):
    creator = fields.ForeignKey(UserResource, 'creator')

    class Meta:
        queryset = TodoList.objects.all()
        resource_name = 'todolists'
        allowed_methods = ['get']


class TodoResource(ModelResource):
    creator = fields.ForeignKey(UserResource, 'creator')

    class Meta:
        queryset = Todo.objects.all()
        resource_name = 'todos'
        allowed_methods = ['get']