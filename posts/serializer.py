from rest_framework import serializers

from .models import Post

# 必要なデータをfieldsに定義
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'content',
            'created_at',
        )

class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'content',
        )