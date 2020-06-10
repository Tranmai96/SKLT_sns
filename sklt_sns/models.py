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
    like = models.ManyToManyField(User, related_name='like')



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='comment')
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
