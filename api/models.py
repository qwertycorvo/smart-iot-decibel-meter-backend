from django.db import models

class DecibelReading(models.Model):
    sensor_id = models.CharField(max_length=50, default="Sensor-001")
    db_value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, default="Cagayan De Oro City")

    def __str__(self):
        return f"{self.sensor_id}: {self.db_value} dB at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
