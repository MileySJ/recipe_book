from email.mime import image
from django.db import models


class Asian(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(blank=True)
    ingrediants = models.TextField(max_length=500)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.title

class Italian(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(blank=True)
    ingrediants = models.TextField(max_length=500)
    description = models.TextField(max_length=800)

    def __str__(self):
        return self.title

    