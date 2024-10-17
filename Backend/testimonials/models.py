from django.db import models

# Create your models here.
class Testimonial(models.Model):
    testimonial = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    author_title = models.CharField(max_length=200)
    author_photo = models.ImageField(upload_to='images')

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return self.testimonial
