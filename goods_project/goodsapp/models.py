from django.db import models

# Create your models here.
class Goods(models.Model):
    goodsname = models.CharField(max_length=100)
    price = models.IntegerField()
    numbers = models.IntegerField()