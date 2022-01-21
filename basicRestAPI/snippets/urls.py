from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # añadir las nuevas rutas de snippet
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]

# urlpatterns = format_suffix_patterns(urlpatterns)  # (, allowed="json") puede añadirse el parametro en la funcion format
