from django.db import models

class News(models.Model):
    titre = models.CharField(max_length=200)
    instagram_link = models.CharField(max_length=400, blank=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    date = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.titre
