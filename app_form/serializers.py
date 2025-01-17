from rest_framework import serializers
from .models import PrimaryChild, ChildHealthInfo, DuplicateChild

class PrimaryChildSerializer(serializers.ModelSerializer):
    fullName = serializers.CharField(required=False) 
    class Meta:
        model = PrimaryChild
        fields = '__all__'

class ChildHealthInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildHealthInfo
        fields = '__all__'

class DuplicateChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = DuplicateChild
        fields = '__all__'