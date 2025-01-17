
from rest_framework.generics import RetrieveUpdateAPIView

from rest_framework.generics import DestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CalendarSerializer
from .models import CalendarEvent
from rest_framework import permissions


# Create your views here.
class CalendarView(APIView):
    permission_classes = [permissions.AllowAny]  # Excludes authentication

    serializer_class = CalendarSerializer

    def get(self, request):
        output = [{"id": output.id,
                   "title": output.title,
                   "date": output.date.isoformat(),
                    "isFinished": output.isFinished,
                  } 
                  for output in CalendarEvent.objects.all()]
        return Response(output) 
    
    def post(self, request):
        serializer = CalendarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)  



class EventDeleteView(DestroyAPIView):
    permission_classes = [permissions.AllowAny]  # Excludes authentication
    queryset = CalendarEvent.objects.all()  # Queryset to fetch the event to delete
    serializer_class = CalendarSerializer  # Serializer for event deletion
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventUpdateView(RetrieveUpdateAPIView):
    permission_classes = [permissions.AllowAny]  # Excludes authentication
    queryset = CalendarEvent.objects.all()  # Queryset to fetch the event to update
    serializer_class = CalendarSerializer  # Serializer for event updating

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














# class CalendarView(generics.CreateAPIView):
#     queryset = CalendarEvent.objects.all()  # Use the 'objects' manager to retrieve all records
#     serializer_class = CalendarSerializer

# class CalendarEventViewSet(viewsets.ModelViewSet):
#     queryset = CalendarEvent.objects.all()  # Use the 'objects' manager to retrieve all records
#     serializer_class = CalendarSerializer

# def main(request):
#     return HttpResponse("Hello")