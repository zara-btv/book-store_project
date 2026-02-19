from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager

class UnpublishedBooksManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=False)


class ListOfBooks(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published=models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='books')
    objects=UnpublishedBooksManager()
    objects = models.Manager()
    unpublished = UnpublishedBooksManager()
    def __str__(self):
        return self.title

class AuthorName(ListOfBooks):
    def __str__(self):
        return self.author
    class Meta:
        proxy = True

class BookImages(models.Model):
    image = models.ImageField(null=True,blank=True)
    book=models.ForeignKey(ListOfBooks, on_delete=models.CASCADE,related_name='images',)
    def __str__(self):
        return str(self.Image)

class CustomApiPermission(models.Model):
    class Meta:
        permissions = (
            ("view_book","owner_only"),
        )