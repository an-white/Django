# serializers
from django.contrib.auth.models import User, Group
from rest_framework import serializers

"""HyperlinkedModelSerializer es bueno para diseños RESTful, 
pero tambien se pueden usar primary key y otros tipos de relaciones"""


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
