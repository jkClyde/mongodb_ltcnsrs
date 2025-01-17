import os
import subprocess
import tempfile
import shutil 
from rest_framework import generics, authentication, permissions
from .models import PrimaryChild, ChildHealthInfo, DuplicateChild
from .serializers import PrimaryChildSerializer, ChildHealthInfoSerializer, DuplicateChildSerializer
from rest_framework.response import Response
from rest_framework import status

from .models import PrimaryChild, ChildHealthInfo, DuplicateChild
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from pathlib import Path


class PrimaryChildListView(generics.ListCreateAPIView):
    queryset = PrimaryChild.objects.all()
    serializer_class = PrimaryChildSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

class PrimaryChildDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PrimaryChild.objects.all()
    serializer_class = PrimaryChildSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

class ChildHealthInfoListView(generics.ListCreateAPIView):
    queryset = ChildHealthInfo.objects.all()
    serializer_class = ChildHealthInfoSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

class ChildHealthInfoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildHealthInfo.objects.all()
    serializer_class = ChildHealthInfoSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

class DuplicateChildCreateView(generics.ListCreateAPIView):
    serializer_class = DuplicateChildSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone

    def get_queryset(self):
        # Filter queryset based on isDuplicate value
        return DuplicateChild.objects.filter(isDuplicate=False)

    def create(self, request, *args, **kwargs):
        # Override the create method to handle the creation of a new DuplicateChild
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Validate and save the data
        self.perform_create(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class DuplicateChildDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DuplicateChild.objects.all()
    serializer_class = DuplicateChildSerializer
    authentication_classes = []  # No authentication required
    permission_classes = [permissions.AllowAny]  # Allow access to everyone


@csrf_exempt
def backup_database(request):
    try:
        # Set the PGPASSWORD environment variable with your database password
        os.environ["PGPASSWORD"] = "group1"

        # Get the user's download directory
        download_dir = Path.home() / "Downloads"

        # Define the path where the backup file will be stored in the Downloads directory
        backup_file_path = download_dir / 'backup.sql'

        # Command to perform the backup using pg_dump
        command = f'pg_dump -U postgres -d db_ltcnsrs -c > {backup_file_path}'


        # Execute the command using shell=True
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, env=os.environ)

        # Read the backup file
        with open(backup_file_path, 'rb') as backup_file:
            response = HttpResponse(backup_file.read())
            response['Content-Disposition'] = 'attachment; filename="backup.sql"'
            return response

    except subprocess.CalledProcessError as e:
        print(f"Backup failed with subprocess error: {e}")
        return HttpResponse("Backup failed", status=500)
    except FileNotFoundError as file_err:
        print(f"File not found error: {file_err}")
        return HttpResponse("File not found", status=500)
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
        return HttpResponse("Internal Server Error", status=500)
    
@csrf_exempt
def restore_database(request):
    try:
        # Set the PGPASSWORD environment variable with your database password
        os.environ["PGPASSWORD"] = "group1"

        # Retrieve the uploaded .sql file from the request
        uploaded_file = request.FILES['file']

        # Get the user's download directory
        download_dir = Path.home() / "Downloads"

        # Define the path where the uploaded file will be stored temporarily in the Downloads directory
        uploaded_file_path = download_dir / 'temp.sql'

        # Write the uploaded file to the temporary location
        with open(uploaded_file_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        # Command to restore the database using psql
        command = f'psql -U postgres -d db_ltcnsrs -f {uploaded_file_path}'

        # Execute the command using shell=True
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, env=os.environ)

        # Cleanup: remove the temporary uploaded file
        os.remove(uploaded_file_path)

        return HttpResponse("Database restored successfully")

    except subprocess.CalledProcessError as e:
        print(f"Restore failed: {e}")
        return HttpResponse("Restore failed", status=500)
    except Exception as ex:
        print(f"An error occurred during restore: {ex}")
        return HttpResponse("Internal Server Error", status=500)