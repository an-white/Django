from rest_framework.decorators import api_view

# basic view with processing data
from rest_framework.response import Response


@api_view(["GET"])
def process_data(request):
    # processing data before send
    lista = [i if (i % 2 == 0) else None
             for i in range(25)]
    # processing data before send
    return Response({
        "list": lista
    })
