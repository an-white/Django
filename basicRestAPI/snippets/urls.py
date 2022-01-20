from django.urls import path
from snippets import views

urlpatterns = [
    # añadir las nuevas rutas de snippet
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),
]
