from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from .models import Post
from .serializer import PostSerializer
from .small_results_set_pagination import SmallResultsSetPagination

import logging

class PostViewSet(viewsets.ModelViewSet):
    
    # TODO:クライアント側のこと考え、エラーメッセージのModelを定義する必要あり
    pagination_class = SmallResultsSetPagination
    page_size = 10
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # def loggingRequest(request):
    #     pass
        # logger = logging.getLogger(__name__)
        # log = 'request method: {} body: {}'
        # log.format((request.method, ruest.data))
        # logger.error(log)
    def get_queryset(self):
        queryset = Post.objects.all()
        name = self.request.query_params.get('name')
        content = self.request.query_params.get('content')
        if content:
            queryset = queryset.filter(content__contains=content)
        if name:
            queryset = queryset.filter(user__username__contains=name)
        return queryset

    # Get　一覧取得
    def list(self, request):
        # self.loggingRequest(request)
        # posts = self.get_queryset()
        page = self.paginate_queryset(self.get_queryset())
        if page is not None:
            serializer = PostSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)

    # Post　新規登録
    def create(self, request):
        # self.loggingRequest(request)
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        content = serializer.validated_data
        serializer.save(user=request.user)
        return Response(status=status.HTTP_200_OK)

    # Get 詳細　/id
    def retrieve(self, request, pk=None):
        # self.loggingRequest(request)
        post = get_object_or_404(self.queryset, pk=pk)
        # Serializeして整形
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    # Put　更新(全部) /id
    def update(self, request, pk=None):
        # self.loggingRequest(request)
        user = request.user
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    
    # Patch 更新(一部) /id
    def partial_update(self, request, pk=None):
        pass
    
    # Delete 削除 /id
    def destroy(self, request, pk=None):
        # self.loggingRequest(request)
        post = get_object_or_404(self.queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_200_OK)
    