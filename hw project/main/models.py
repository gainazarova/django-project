from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self): return f'{self.title} - {self.price}'
