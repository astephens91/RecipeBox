from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=250, default='INSERT BIO')

    def __str__(self):
        return self.name


class RecipeItem(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='TITLE OF RECIPE')
    description = models.TextField(default='RECIPE DESCRIPTION')
    time = models.IntegerField(default=1)
    instructions = models.TextField(default='RECIPE INSTRUCTIONS')
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
