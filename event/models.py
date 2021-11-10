from django.db import models


class Event(models.Model):
    titre = models.CharField(max_length=200)
    Text = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='event/', null=True, blank=True)
    date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titre
