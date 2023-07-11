from django.contrib import admin
from .models import *


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']

@admin.register(Images)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['post', 'image']
