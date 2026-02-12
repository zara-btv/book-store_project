from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from Book.views import AccessBook


class CustomUserManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class AllobjectsUser(UserManager):
    def get_queryset(self):
        return super().get_queryset()

# Create your models here.
class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=11,unique=True,null=True,blank=True)
    national_id=models.CharField(max_length=10,unique=True,null=True,blank=True)
    is_deleted=models.BooleanField(default=False)

    objects=CustomUserManager()
    all_objects=AllobjectsUser()

class CustomPermission(models.Model):
    class Meta:
        permissions = (
            ("Blue", "Can drive"),
            ("Yellow", "Can vote in elections"),
            ("Red", "Can drink alcohol"),
        )