from django.conf.urls import url, include, patterns

from tastypie.api import Api

from api import resources


v1_api = Api(api_name='v1')
v1_api.register(resources.UserResource())
v1_api.register(resources.TodoListResource())
v1_api.register(resources.TodoResource())

urlpatterns = patterns('',
    url(r'^', include(v1_api.urls)),
)
