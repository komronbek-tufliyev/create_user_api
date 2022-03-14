from django import forms
from .models import CustomUser
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField

GENDER_CHOICES = (
    ('Erkak', 'Erkak'),
    ('Ayol', 'Ayol')
)

class CreateUserForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    gender = forms.RadioSelect(choices=GENDER_CHOICES)
    phone_number = PhoneNumberField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = CustomUser
        fields = '__all__'