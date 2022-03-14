from .views import UserCreateView
from django.urls import path
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework_swagger.renderers import 

# schema_view = get_swagger_view(title='User Creation Form API')

urlpatterns = [
    path('add/', UserCreateView.as_view(), name='add_user_api'),
    # path('v1/schema/', schema_view),	
]