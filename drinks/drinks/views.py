from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3


@api_view(['GET'])
def say_hello(request):
    db = boto3.resource('dynamodb')
    table = db.Table('drinks')
    drinks = table.scan()
    return Response({'drinks': drinks.get('Items')})