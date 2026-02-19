
from django.urls import path,include
from Book.views import *
# from django.conf.urls.static import static
from BookStore import settings

urlpatterns = [
    path('text/',index),
    path('view-books/',AccessBook.as_view()),
    path('published-book/',PublishedBooks.as_view()),
]
