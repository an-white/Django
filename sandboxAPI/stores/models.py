from django.db import models

STORE_CATEGORY = [
    ('tech', 'Tech'),
    ('food', 'Food'),
    ('clothes', 'Clothes'),
    ('shoes', 'Shoes'),
    ('home', 'Home')
]


class Store(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, default="my Store")
    category = models.CharField(choices=STORE_CATEGORY, default="tech", max_length=120)
    revenue = models.FloatField(default=0.0)

    # owner = models.ForeignKey()

    class Meta:
        ordering = ["name"]
