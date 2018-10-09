from django.db import models


class PartnersInformation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=5000, blank=True)
    url = models.CharField(max_length=256)
    image_url = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title
