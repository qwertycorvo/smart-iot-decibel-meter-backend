from rest_framework import serializers
from .models import DecibelReading

class DecibelReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = DecibelReading
        fields = '__all__'