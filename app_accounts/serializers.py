from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers



User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 
                  'barangay', 'phone_number', 'job_description',
                    'is_approved','is_admin', 'is_disabled')


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'last_login', 'is_superuser', 'job_description', 'is_active', 'is_staff', 'is_admin', 'is_approved',
                   'is_disabled', 'groups', 'user_permissions', 'id', 'email']

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         # The default result (access/refresh tokens)
#         data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
#         # Custom data you want to include
#         data.update({'user': self.user.email})
#         data.update({'id': self.user.id})
#         data.update({'is_admin': self.user.is_admin})
#         # and everything else you want to send in the response
#         return data
