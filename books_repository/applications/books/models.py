from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=120, blank=False, null=False)
    last_name = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Genre(models.Model):
    type = models.CharField(max_length=120, blank=False, null=False)


class Book(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    genre = models.ForeignKey(Genre, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
