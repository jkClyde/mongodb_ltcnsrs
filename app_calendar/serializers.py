from rest_framework import serializers
from .models import CalendarEvent

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model =  CalendarEvent
        fields = ('id','title', 'date', 'isFinished')