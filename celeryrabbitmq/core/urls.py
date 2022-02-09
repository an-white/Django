from django.contrib import admin
from django.urls import path

from task2.views import ReviewEmailView

"""
    añadiendo la vista del form de email
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reviews/', ReviewEmailView.as_view(), name="reviews"),
]
