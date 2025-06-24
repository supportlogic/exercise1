from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from mlapp.models import Customer, DataSource
from rest_framework.authentication import TokenAuthentication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def get_data_sources(request):
    try:
        customer = Customer.objects.get(name=request.user.username)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found for user'}, status=status.HTTP_404_NOT_FOUND)
    data_sources = DataSource.objects.filter(customer=customer)
    data = [
        {'pk': ds.pk, 'name': ds.name, 'created_at': ds.created_at, 'updated_at': ds.updated_at}
        for ds in data_sources
    ]
    return Response({'data_sources': data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def add_data_source(request):
    try:
        customer = Customer.objects.get(name=request.user.username)
    except Customer.DoesNotExist:
        return Response({'error': 'Customer not found for user'}, status=status.HTTP_404_NOT_FOUND)
    name = request.data.get('name')
    if not name:
        return Response({'error': 'Missing name'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        ds = DataSource.objects.create(customer=customer, name=name)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'pk': ds.pk, 'name': ds.name, 'created_at': ds.created_at, 'updated_at': ds.updated_at})

