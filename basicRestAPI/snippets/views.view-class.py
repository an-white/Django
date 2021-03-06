from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer

# adding enpoints for our user model
from django.contrib.auth.models import User

# add required permissions to views
from rest_framework import permissions

# custom permissions
from snippets.permissions import IsOwnerOrReadOnly

# creating an endpoint for the root of our API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers


# using generic class-based views
# this allows makes more compact view class and easy
class SnippetList(generics.ListCreateAPIView):
    """
    list all snippets or cretea a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # IsAuthenticatedOrReadOnly wil ensure that authenicated request get read-write access and the unauthenticated requests get read-only access
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # add serialized representaion of the user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    detailed snippet view, we can update and delete it
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # IsAuthenticatedOrReadOnly wil ensure that authenicated request get read-write access and the unauthenticated requests get read-only access
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


# create an endpoint for the higlighted snippets
class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
