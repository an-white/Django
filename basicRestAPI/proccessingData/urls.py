from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from views import process_data

urlpatterns = format_suffix_patterns([
    path("testing", process_data, name="testing")
])
