from rest_framework import serializers
from User.models import CustomUser

class RegisterUserSerializer(serializers.ModelSerializer):
    shamsi_birth_day=serializers.SerializerMethodField(read_only=True)
    def get_shamsi_birth_day(self,obj):
        return "1404-11-24"
    def validate_phone_number(self, value):
        if len(value) <3:
            raise serializers.ValidationError('phone number is not correct')
        return value

    class Meta:
        model = CustomUser
        fields=["username","phone_number","password","shamsi_birth_day"]
        extra_kwargs = {'password': {'write_only': True}}
    #     for checking the password

    def create(self, validated_data):
        user= CustomUser(
            phone_number=validated_data['phone_number'],
            username=validated_data['username'],
        )
        return user