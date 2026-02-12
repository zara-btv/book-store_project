
from django.urls import path,include
from Book.views import *

urlpatterns = [
    path('text/',index),
    path('view-books/',AccessBook.as_view()),

]