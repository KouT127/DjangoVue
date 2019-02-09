from rest_framework import serializers
from .models import Post

# 必要なデータをfieldsに定義
class PostSerializer(serializers.ModelSerializer):
    # validationを記述
    content = serializers.CharField(min_length=1,max_length=140)

    class Meta:
        model = Post
        fields = (
            'content',
            'created_at',
            'updated_at'
        )
        read_only_fields = ()
        extra_kwargs = {}
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)