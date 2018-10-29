from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    last_name = models.CharField(max_length=120, blank=False, null=False)


class Book(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
