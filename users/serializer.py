from rest_framework import serializers

from .models import User

# 必要なデータをfieldsに定義
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'name',
            'email',
        )

