from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Post
from .serializer import PostSerializer, AddPostSerializer
import logging


class PostViewSet(viewsets.ModelViewSet):
    # Get
    logger = logging.getLogger(__name__)
    logger.error('Posts get')
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # Post
    def create(self, request):
        logger = logging.getLogger(__name__)
        logger.error('Posts post')
        user = request.user
        return Response({'user': user.username})
