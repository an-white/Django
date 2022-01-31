from rest_framework import serializers
from stores.models import Store


class StoreSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Store
        fields = ['id', 'name', 'category', 'revenue', 'created']
