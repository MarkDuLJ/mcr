from django.db import models


class Product(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    material = models.CharField(max_length=100)
    spec = models.IntegerField()



