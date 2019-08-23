from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profil_pics", default="profil.png")
    information = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profil'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            img_size = (300, 300)
            img.thumbnail(img_size)
            img.save(self.image.path)