from django.contrib import admin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'phone_number', 'created_at')

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUserAdmin)