from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def home(request):
    serializer_data={
        'message': 'Hello World!',
        'status': 200
    }
    return Response(serializer_data)
