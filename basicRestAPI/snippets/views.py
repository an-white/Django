from rest_framework import generics

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# using generic class-based views
# this allows makes more compact view class and easy
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
