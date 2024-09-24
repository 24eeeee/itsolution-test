from django.db import models


class Request(models.Model):
    message = models.CharField(max_length=1024)
    timestamp = models.DateTimeField()
