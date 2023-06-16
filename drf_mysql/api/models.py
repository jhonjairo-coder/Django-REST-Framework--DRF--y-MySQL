from django.db import models


class Company(models.Model):
    Name = models.CharField(max_length=50)
    website = models.URLField( max_length=200)
    foundation = models.PositiveIntegerField()