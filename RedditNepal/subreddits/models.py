from django.db import models
from django.utils.text import slugify
import misaka
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.library

class SubReddit(models.Model):
    name = models.CharField(max_length=255,unique = True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='SubRedditMember')

    def __str__(self):
        return self.name

    def slug(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('subreddits:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class SubRedditMember(models.Model):
    subreddit = models.ForeignKey(SubReddit,related_name="memberships",on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name="user_subreddits",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('subreddit','user')
