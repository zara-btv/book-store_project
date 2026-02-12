from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from Book.models import *
from Book.serializer import AccessBookSerializer


def index(request):
    return HttpResponse('hi , I am working!')

class AccessBook(generics.ListCreateAPIView):
    queryset = ListOfBooks.objects.all()
    serializer_class = AccessBookSerializer



