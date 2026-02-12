from rest_framework import serializers
from Book.models import ListOfBooks


class AccessBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListOfBooks
        fields = '__all__'