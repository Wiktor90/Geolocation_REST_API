from django.db import models


class Geodata (models.Model):

    ip = models.CharField(max_length=50)
    continent_name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)

    def __str__(self):
        return self.ip
