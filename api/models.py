from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=250, blank=False)
    dob = models.DateField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=250, blank=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Category(models.Model):
    name = models.CharField(max_length=250, blank=False)
    description = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.BooleanField(default=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250, blank=False)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, editable=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
