from django.urls import path
from ColorBook.views import Index


urlpatterns = [
    path('blue/',Index.as_view(), name='index'),
]