from rest_framework import serializers

from .models import User

# 必要なデータをfieldsに定義
class UserSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
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
        extra_kwargs = {
            'image': {'write_only': True}
        }

    def get_image_url(self, obj):
        return obj.image.url
        # request = self.context.get('request')
        # image_url = user.image.url
        # return request.build_absolute_uri(image_url)