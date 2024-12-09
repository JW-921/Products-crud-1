from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True)
    description = models.TextField(null=True)
