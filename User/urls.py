
from django.urls import path,include
from User.views import RegisterUserView, myview

urlpatterns = [
path('signup/', RegisterUserView.as_view()),
]
