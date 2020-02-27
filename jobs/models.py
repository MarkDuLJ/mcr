from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    material = models.CharField(max_length=100)
    spec = models.IntegerField()

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantities = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantities = models.IntegerField()


class Engineer(models.Model):
    name = models.CharField(max_length=50)
    work_hours = models.IntegerField()
