from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profil_pics", default="profil.png")
    information = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profil'