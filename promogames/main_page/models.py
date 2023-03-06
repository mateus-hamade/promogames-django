from django.contrib.auth.models import User
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
    developer = models.CharField(max_length=100, null=True)
    release_date = models.CharField(max_length=100, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receive_promotions = models.EmailField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    type = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment