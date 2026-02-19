
from django.urls import path,include
from User.views import RegisterUserView, Users

urlpatterns = [
path('signup/', RegisterUserView.as_view()),
path('all_user', Users.as_view())
]
