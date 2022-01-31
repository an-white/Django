from rest_framework import viewsets

# Create your views here.
from stores.serializers import StoreSerializer
from stores.models import Store


class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
