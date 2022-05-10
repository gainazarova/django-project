from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    def __str__(self): return f'{self.name} {self.last_name}'

class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField()
    def __str__(self): return f'{self.author}:{self.name}'


