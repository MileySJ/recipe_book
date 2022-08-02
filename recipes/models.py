from email.mime import image
from django.db import models


class Asian(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(blank=True)
    ingredients = models.TextField(max_length=1_000, blank=True, null=True)
    description = models.TextField(max_length=1_000)

    def __str__(self):
        return self.title

class Italian(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(blank=True)
    ingredients = models.TextField(max_length=1_000, blank=True, null=True)
    description = models.TextField(max_length=1_000)

    def __str__(self):
        return self.title

    