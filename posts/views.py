from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Post
from .serializer import PostSerializer, AddPostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @detail_route(methods=['post'])
    def add_post(self, request, pk):
        user = request.user 
        # user = self.get_object()
        serializer = AddPostSerializer(data=request.data)
        if serializer.is_valid():
            user.post_set.create(content=serializer.Meta)
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)