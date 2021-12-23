from blog.models import Category, Post, Comment
from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
class PostBlogAdmin( admin.ModelAdmin ):
    list_display = ('id', 'title', 'slug', 'author', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at',)
    search_fields = ['title', 'content']

admin.site.register( Category )
admin.site.register( Post, PostBlogAdmin )
admin.site.register( Comment )