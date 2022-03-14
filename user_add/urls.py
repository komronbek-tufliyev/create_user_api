from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path('add/', CreateUserView.as_view(), name='create_user'),
]