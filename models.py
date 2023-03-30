from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=70)
    desc = models.TextField()

