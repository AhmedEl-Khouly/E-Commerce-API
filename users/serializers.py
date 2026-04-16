from .models import *
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "email", "password", "password_confirm","username",'first_name', 'last_name',"phone_number", "address", "bio", "profile_image"]
        extra_kwargs = {
            "password": {'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = CustomUser.objects.create_user(**validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email","username",'first_name', 'last_name',"phone_number", "address", "bio", "profile_image", "created_at", 'updated_at']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ["user"]
        extra_kwargs = {
            "user": {"read_only": True}
        }

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "address",
            "bio",
            "profile_image"
        ]
        extra_kwargs = {
            "email": {"read_only": True}
        }
