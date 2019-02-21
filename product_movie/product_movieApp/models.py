from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=3, max_digits=9)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
