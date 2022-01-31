from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
    name = models.CharField(max_length=150, default="")
    store = models.ForeignKey('stores.store', related_name="products", on_delete=models.CASCADE)
