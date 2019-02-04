from rest_framework import serializers
from .models import Post

# 必要なデータをfieldsに定義
class PostSerializer(serializers.ModelSerializer):

    content = serializers.CharField(min_length=10,max_length=140)

    class Meta:
        model = Post
        fields = (
            'content',
            'created_at',
        )
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)