from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer



@api_view(['GET'])
def ProfileView(request):
    profile = request.user.profile
    serializer = ProfileSerializer(profile)
    return Response(serializer.data)

