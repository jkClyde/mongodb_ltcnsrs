from django.urls import path, include
from .views import AuditCreateView
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('calendar/', CalendarView.as_view(),  name='event-list'), 
    # path('events/<int:pk>/', EventDeleteView.as_view(), name='event-delete'),
    path('auditcreate/', AuditCreateView.as_view(), name='audit-create')

]
    