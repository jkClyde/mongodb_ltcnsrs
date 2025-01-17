from django.urls import path
from . import views
from .views import  backup_database, PrimaryChildListView, PrimaryChildDetailView, ChildHealthInfoListView, ChildHealthInfoDetailView, DuplicateChildCreateView, DuplicateChildDetailView
urlpatterns = [
    path('primarychild/', PrimaryChildListView.as_view(), name='primarychild-list'),
    path('primarychild/<int:pk>/', PrimaryChildDetailView.as_view(), name='primarychild-detail'),
    path('duplicateChild/', DuplicateChildCreateView.as_view(), name='duplicate-list'),
    path('duplicateChild/<int:pk>/',DuplicateChildDetailView.as_view(), name='duplicate-detail'),

    path('childhealthinfo/', ChildHealthInfoListView.as_view(), name='ChildHealthInfo-list'),
    path('childhealthinfo/<int:pk>/', ChildHealthInfoDetailView.as_view(), name='ChildHealthInfo-detail'),
    path('backup/', backup_database, name='backup_database'),
    path('restore/', views.restore_database, name='restore_database'),   


]