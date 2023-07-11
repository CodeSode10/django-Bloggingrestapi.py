from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Images(models.Model):
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="images")
