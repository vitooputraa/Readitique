from django.db import models
from django.contrib.auth.models import User
from main.models import Book

class NewBook(models.Model):
    index_key = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=255)
    rating = models.FloatField(default=0)
    image_link = models.URLField(max_length=300, default="https://img.freepik.com/premium-vector/open-blank-book-illustration-school-supply-back-school-open-book-icon-reading-writing_502505-530.jpg?w=2000")
    count_read = models.PositiveIntegerField(default=0)
    votes = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(NewBook, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'book')