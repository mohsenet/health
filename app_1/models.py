from django.db import models


class Health(models.Model):
    date = models.CharField(max_length=100)
    toothbrush = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
