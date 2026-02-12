from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from User.models import CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # search_fields = ('username',)
    def get_queryset(self, request):
        qs=self.model.all_objects.get_queryset()
        ordering=self.ordering or ()
        if ordering:
            qs=qs.order_by(*ordering)
        return qs



# Register your models here.
