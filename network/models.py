from django.db import models

class SpeedTestResult(models.Model):
    download_speed = models.FloatField()
    upload_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)