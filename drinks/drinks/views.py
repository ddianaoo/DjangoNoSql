from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3


@api_view(['GET', 'POST'])
def say_hello(request):
    db = boto3.resource('dynamodb')
    table = db.Table('drinks')

    if request.method == 'GET':
        drinks = table.scan()
        return Response({'drinks': drinks.get('Items')})

    elif request.method == 'POST':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response({'error': 'Failed to add'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_info(request, name):
    db = boto3.resource('dynamodb')
    table = db.Table('drinks')

    if request.method == 'GET':
        try:
            drink = table.get_item(Key={'name': name})
            item = drink['Item']
            return Response({'drink': item}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'NOT FOUND'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'PUT':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Failed to update'}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            table.delete_item(Key={'name': name})
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Failed to delete'}, status=status.HTTP_400_BAD_REQUEST)