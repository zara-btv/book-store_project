from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from User.permissions import HasBluePermission
from rest_framework.views import APIView

class Index(APIView):
    permission_classes = [IsAuthenticated,HasBluePermission]
    def get(self, request):
        return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.
