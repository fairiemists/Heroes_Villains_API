from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from supers.models import Super
from ..supers.serializers import SuperSerializer
from .serializers import SuperTypeSerializer
from .models import SuperType

@api_view(['GET'])
def super_types_list(request):

    type_param = request.query_params.get('type')
    supers = Super.objects.all()
    custom_response = {}
    super_types = SuperType.objects.all()

    if type_param:
        supers = supers.filter(super_type__type=type_param)
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    else:
        for super_type in super_types:
            heroes = Super.objects.filter(super_type_id=1)
            hero_serializer = SuperSerializer(heroes, many=True)
            villains = Super.objects.filter(super_type_id=2)
            villain_serializer = SuperSerializer(villains, many=True)
            custom_response = {
                "heroes": hero_serializer.data,
                "villains": villain_serializer.data
            }
        return Response(custom_response)

