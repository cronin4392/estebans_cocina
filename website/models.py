from django.db import models
from autoslug import AutoSlugField

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from='title')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title