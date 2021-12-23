from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.shortcuts import reverse
from hitcount.models import HitCount
from taggit.managers import TaggableManager

User = get_user_model()

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = AutoSlugField(populate_from='title', unique=True)
    thumbnail = models.ImageField(
        default='default/default_blog_post_img1.png', upload_to='thumbnails/', blank=True, null=True)
    image_url = models.CharField(
        default=None, max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_at']

    @property
    def post_link(self):
        return reverse('post', kwargs={
            'slug': self.slug,
        })

    @staticmethod
    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.title + ' | ' + self.slug + ' | ' + str(self.author)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_at').all()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False

    def __str__(self):
        return str('%s | %s' % (self.user.username, self.created_at.strftime('%d-%m-%Y')))
