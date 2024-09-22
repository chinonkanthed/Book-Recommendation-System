from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rating = models.FloatField(null=True, blank=True)
    votes = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    read_url = models.URLField(max_length=400, blank=True, null=True)
    buy_url = models.URLField(max_length=400, blank=True, null=True)

    def __str__(self):
        return self.title