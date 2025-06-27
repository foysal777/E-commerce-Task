from rest_framework import serializers
from .models import Profile, User , ImageUploadCloudinary

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploadCloudinary
        fields = '__all__'
