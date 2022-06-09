from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from .views import UserViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
