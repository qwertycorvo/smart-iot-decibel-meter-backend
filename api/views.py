from rest_framework import generics
from .models import DecibelReading
from .serializers import DecibelReadingSerializer

class ReadingListAPIView(generics.ListCreateAPIView):
    queryset = DecibelReading.objects.all()[:50]  # Get last 50 readings
    serializer_class = DecibelReadingSerializer

class ReadingLatestAPIView(generics.RetrieveAPIView):
    serializer_class = DecibelReadingSerializer
    
    def get_object(self):
        return DecibelReading.objects.first()
