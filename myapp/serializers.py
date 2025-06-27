from rest_framework import serializers
from .models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # Optional: add custom claims
#         token['email'] = user.email
#         return token
