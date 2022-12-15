from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3


@api_view(['GET'])
def say_hello(request):
    return Response({"test": "data"})