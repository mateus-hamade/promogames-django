from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100, unique=True)
    store = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, null=True)
    link_url = models.CharField(max_length=100)
    discount_price = models.CharField(max_length=100)

    tag = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title