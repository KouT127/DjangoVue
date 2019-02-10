from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FormParser, MultiPartParser 
from .models import User
from .serializer import UserSerializer
import logging


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,) 
    parser_classes = (FormParser, MultiPartParser) 

    def update(self, request, pk=None):
        user = request.user
        serializer = UserSerializer(user, data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
