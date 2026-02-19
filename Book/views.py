from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from Book.permissions import UniqueApiPermission
from Book.models import *
from Book.serializer import AccessBookSerializer
from django.db.models import Sum,Count,Avg
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes

# import models

def index(request):
    return HttpResponse('hi , I am working!')

class AccessBook(generics.ListCreateAPIView):
    permission_classes = [UniqueApiPermission]
    serializer_class = AccessBookSerializer

    def get_queryset(self):
        return ListOfBooks.objects.annotate(
            total_images=Count("images")
        )

    parser_classes = [MultiPartParser, FormParser]



class PublishedBooks(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AccessBookSerializer
    queryset = ListOfBooks.objects.filter(is_published=True)



