from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user_add.models import CustomUser, UserProfile
from .serializers import CustomuserSerializer
# Create your views here.

class UserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomuserSerializer
    permission_classes = (AllowAny, )
