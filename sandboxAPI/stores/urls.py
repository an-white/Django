from django.urls import path
from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

from stores.views import StoreViewSet

store_list = StoreViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

store_details = StoreViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('stores/', store_list, name='store-list'),

])
