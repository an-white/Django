from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User

# Uso de ModelSerializers
"""
 permite acortar la creacion de clases serializadas, 
 determina automaticamente un conjunto de campos 
 simplifica la implementacion del create and update
"""


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']

    # updating snippet serializer associating the snippet with the user that created it
    owner = serializers.ReadOnlyField(source="owner.username")
    # ReadOnlyField is untyped field and always will be used for serialized representation


class UserSerializer(serializers.ModelSerializer):
    # snippets is a reverse relationship with
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
