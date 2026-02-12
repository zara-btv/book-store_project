from rest_framework import serializers
from User.models import CustomUser

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields=["username","phone_number","password"]
        extra_kwargs = {'password': {'write_only': True}}
    #     for checking the password

    def create(self, validated_data):
        user= CustomUser(
            phone_number=validated_data['phone_number'],
            username=validated_data['username'],
        )
        return user