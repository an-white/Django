from django.urls import path, include
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up my API using automatic URL routing
# Additionally, we include login URLs for the browsable API

urlpatterns = [
    path('', include(router.urls)),
    path('polls/', include('polls.urls')),
    # path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # wire up the app snippets urls to the main urls of the project
    path('', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
