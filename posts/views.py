from rest_framework import status
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from .serializer import PostSerializer
import logging


class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # Get　一覧取得
    def list(self, request):
        logger = logging.getLogger(__name__)
        logger.error('request get')
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Post　新規登録
    def create(self, request):
        logger = logging.getLogger(__name__)
        logger.error('request body: %s', request.data)
        user = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data
            user.post_set.create(content=content)
            user.save()
            return Response({}, status=status.HTTP_200_OK)

    # Get 詳細　/id
    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        # Serializeして整形
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    # Put　更新(全部) /id
    def update(self, request, pk=None):
        pass
    
    # Patch 更新(一部) /id
    def partial_update(self, request, pk=None):
        pass
    
    # Delete 削除 /id
    def destroy(self, request, pk=None):
        pass

