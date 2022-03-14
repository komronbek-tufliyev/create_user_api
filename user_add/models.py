from enum import unique
from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
# from .forms import GENDER_CHOICES

# Create your models here.
class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    
    GENDER_CHOICES = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol')
    )
    gender = models.CharField(max_length=5, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField(max_length=16, unique=True, blank=False, null=False)
    password = models.CharField(max_length=64)
    confirm_password = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # phone_validator = RegexValidator(regex=r'^\+?1?\d{9,15}$', message='Your phone number doesn\'t match')

    def __str__(self) -> str:
        return self.name

    
class UserProfile(models.Model):

    REQUIRED_FIELDS = ('customuser',)

    user = models.OneToOneField(CustomUser, related_name='profile', unique=True, on_delete=models.CASCADE)