from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=200, null=True)
	id_num = models.FloatField()
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name



class Post(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


class Ine(models.Model):
    ip_address = models.CharField('IPアドレス', max_length=20)
    parent = models.ForeignKey(Post, on_delete=models.CASCADE) 


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
