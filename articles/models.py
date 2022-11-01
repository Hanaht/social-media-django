from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
class Article(models.Model):
    title = models.CharField(max_length=255
    )
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE,
    )
    likes = models.ManyToManyField(get_user_model(), blank=True, related_name='likes')
    dislikes = models.ManyToManyField(get_user_model(), blank=True, related_name='dislikes')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=400)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.comment[:60]
class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title