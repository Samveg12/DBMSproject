from django.urls import path
from django.urls.resolvers import URLPattern
from source.api.views import (api_detail,dis_detail,update_api,delete_api,create_api)

app_name='source'

urlpatterns = [
    path('country/<slug>/', api_detail,name="api_detail"),
    path('disaster/<slug>/', dis_detail,name="dis_detail"),
    path('disaster/<slug>/update', update_api,name="update_api"),
    path('disaster/<slug>/delete', delete_api,name="delete_api"),
    path('disaster/create', create_api,name="create_api"),

]