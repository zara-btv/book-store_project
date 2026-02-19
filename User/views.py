from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import generics

from User.models import CustomUser
# from User.permissions import HasBluePermission
from User.serializer import RegisterUserSerializer




class RegisterUserView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer_class = RegisterUserSerializer(data=request.data)
        if serializer_class.is_valid():
            user=serializer_class.save()
            user.set_password(request.data['password'])
            user.save()
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"result":{"user_id":user.id}},status=status.HTTP_200_OK)


class Users(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
    queryset = CustomUser.objects.all()