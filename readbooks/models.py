from django.db import models
from django.contrib.auth.models import User



class books(models.Model):
    isbn = models.CharField(max_length=32)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    year = models.IntegerField()
    rating_count = models.IntegerField(default=0)
    avg_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title
   

class Review(models.Model):
    title = models.CharField(max_length=64)
    bookid = models.ForeignKey(books, on_delete=models.CASCADE)
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.title