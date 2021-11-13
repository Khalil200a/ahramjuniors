from django.db import models


class Article(models.Model):
    titre = models.CharField(max_length=200)
    image = models.ImageField(upload_to='article/image/', null=True, blank=True)
    date = models.CharField(max_length=200, blank=True)
    document = models.FileField(upload_to='article/doc', null=True, blank=True)

    def __str__(self):
        return self.titre
