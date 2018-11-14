from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=30)
    book_price = models.IntegerField()
    book_author = models.CharField(max_length=50)
    created_at = models.DateField()
# Create your models here.
