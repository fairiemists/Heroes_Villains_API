from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET', 'PUT', 'DELETE'])
def super_types_list(request, pk):
    super_type = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(super_type);
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(super_type, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        super_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

