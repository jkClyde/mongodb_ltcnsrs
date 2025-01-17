from django.http import JsonResponse

from django.views import View
import requests
from rest_framework import permissions
from .serializers import UserCreateSerializer, UserEditSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import generics
from .models import UserAccount
from rest_framework import generics, permissions


from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import Token
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveUpdateAPIView







class UserActivationView(View):
    permission_classes = [permissions.AllowAny]  # Excludes authentication
    def get(self, request, uid, token):
        post_url = "http://localhost:8000/auth/users/activation/"
        post_data = {'uid': uid, 'token': token}

        try:
            result = requests.post(post_url, data=post_data)
            content = result.text
            return JsonResponse({"message": "Successfully Activated. You may now login at http://localhost:5173/login"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
        

class UserListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]  # Excludes authentication
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer


class UserApprovalView(View):
    def get(self, request, user_id, action):
        try:
            user = UserAccount.objects.get(id=user_id)
            if action == 'approve':
                user.is_approved = True
                user.save()
                return JsonResponse({"message": "User approved successfully"})
            elif action == 'deny':
                user.delete()
                return JsonResponse({"message": "User registration denied"})
            else:
                return JsonResponse({"error": "Invalid action"})
        except UserAccount.DoesNotExist:
            return JsonResponse({"error": "User not found"})
        

class DisableUserView(generics.UpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_disabled = True
        user.save()
        return Response(data={'message': 'User has been disabled'}, status=status.HTTP_200_OK)

class EnableUserView(generics.UpdateAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_disabled = False
        user.disabled_at = None
        user.save()
        return Response(data={'message': 'User has been enabled'}, status=status.HTTP_200_OK)
    

def create_jwt_token(user):
    token = Token()
    token['is_admin'] = user.is_admin  # Include is_admin in the payload
    return str(token)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: UserAccount):
        token = super().get_token(user)

        token['email'] = user.email
        token['user_id'] = user.id
        token['full_name'] = user.first_name + " " + user.last_name
        token['is_admin'] = user.is_admin
        return token


class DeleteUserView(generics.DestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserCreateSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EditUserView(RetrieveUpdateAPIView):
    queryset = UserAccount.objects.all()
    permission_classes = [permissions.AllowAny]  # Add your authentication logic

    def get_serializer_class(self):
        # Use different serializers for create and edit operations
        if self.request.method == 'PUT':
            return UserEditSerializer
        else:
            return UserCreateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer