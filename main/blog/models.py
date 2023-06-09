from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True, null=True)
    image = models.CharField(max_length=200, null=True, blank=False)

    def __str__(self):
        return self.title