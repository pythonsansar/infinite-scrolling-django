from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    image = models.ImageField(blank=True, upload_to='book_images')

    def __str__(self):
        return self.title
