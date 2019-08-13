from django.shortcuts import render
from django.http import HttpResponse
from .models import Actor
from rest_framework.decorators import api_view
from .serializers import ActorSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['get'])
def fetch_personas(request):
    #fetch all the actor objects
    personas = Personas.objects.all()
    #serialize the actors
    serializer = PersonasSerializer(personas, many=True)
    #return Response using rest_framework's response
    return Response(serializer.data)