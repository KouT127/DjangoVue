from rest_framework import serializers

from .models import User

# 必要なデータをfieldsに定義
class UserSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'full_name',
            'date_joined',
            'image',
            'image_url'
        )
        read_only_fields = ('image_url',)
        # fieldsには、記述するが返したくない場合下記に記入
        extra_kwargs = {
            'image': {'write_only': True}
        }

    def get_image_url(self, obj):
        return obj.image.url