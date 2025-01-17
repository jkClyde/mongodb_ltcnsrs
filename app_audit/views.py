from rest_framework import generics, authentication, permissions
from .models import Audit
from .serializers import AuditSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AuditCreateView(generics.ListCreateAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone