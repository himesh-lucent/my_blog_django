from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=15)
    slug = models.CharField(max_length=150)
    post_images = models.ImageField(upload_to='postimg')

    def __str__(self):
        return self.title + ' ' + self.author