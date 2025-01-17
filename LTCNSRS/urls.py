from django.urls import path, include, re_path
from django.contrib import admin

from django.views.generic import TemplateView
from app_accounts.views import UserActivationView, DeleteUserView
from app_accounts.views import UserListView, UserApprovalView, DisableUserView, EnableUserView, CustomTokenObtainPairView, EditUserView
from app_audit.views import AuditCreateView



urlpatterns = [
    path('admin/', admin.site.urls),  # Add this line for the admin interface
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/users/activation/<str:uid>/<str:token>/',
         UserActivationView.as_view(), name='UserActivationView'),
    path('', include('app_form.urls')),
    path('', include('app_calendar.urls')),
    path('user_approval/<int:user_id>/<str:action>/', UserApprovalView.as_view(), name='user_approval'),
    path('users/<int:pk>/disable/', DisableUserView.as_view(), name='disable_user'),
    path('users/<int:pk>/enable/', EnableUserView.as_view(), name='enable_user'),
    path('users/<int:pk>/delete/', DeleteUserView.as_view(), name='delete_user'),
    path('api/users/<int:pk>/edit/', EditUserView.as_view(), name='edit-user'),



    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('audit/', AuditCreateView.as_view(), name='Audit-Create'),


]
