from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # add new snippet routes
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # add users views
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # add login to the browsable API
    #path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)  # (, allowed="json") puede añadirse el parametro en la funcion format
