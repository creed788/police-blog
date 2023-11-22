from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    post_image = models.ImageField(null=True, upload_to='post_images/')
    sub_title = models.CharField(max_length=500, null = True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

class FAQ(models.Model):
    question = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(auto_now_add = True)

class Answer(models.Model):
    answer = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    