from django.db import models

# Create your models here.
class main_page(models.Model):
    title = models.CharField(max_length=100, unique=True)
    store = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100)
    link_url = models.CharField(max_length=100)
    discount_price = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title