from rest_framework import serializers
from user_add.models import CustomUser, UserProfile

class CustomuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}} 
    
    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        UserProfile.objects.create(user=user)
        return user
