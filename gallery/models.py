from django.db import models


class Photo(models.Model):
    image = models.ImageField(upload_to='gallery/image/', null=True, blank=True)


class Video(models.Model):
    image = models.ImageField(upload_to='gallery/image/', null=True, blank=True)
    video = models.FileField(upload_to='gallery/video/', null=True, blank=True)
