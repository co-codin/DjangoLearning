from django.db import models

# Create your models here.
class Ebook(models.Model):
    title = models.CharField(max_length=140)
    author = models.CharField(max_length=60)
    description = models.TextField()
    publication_date = models.DateTimeField()

    def __str__(self):
        return self.title
