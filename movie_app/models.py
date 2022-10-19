from django.db import models


class Director(models.Model):
    name = models.CharField(null=False, max_length=100)


class Movie(models.Model):
    title = models.CharField(null=False, max_length=100)
    description = models.TextField()
    duration = models.IntegerField(default=60)
    director = models.ForeignKey


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey
