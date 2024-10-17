from django.db import models


# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    icon = models.CharField(max_length=30) ## icon name

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title