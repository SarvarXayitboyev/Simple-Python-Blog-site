from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.forms import DateTimeField
from django.utils import timezone


# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status="published")


class Post(models.Model):
    STATUS =(
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_data="publish")
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="blo_post")
    body = models.TextField()
    publish = models,DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS,default='draft')


    class Meta:
        ordering =('-published',)


    def __str__(self):
        return self.title


    objects = models.Manager()
    published= PublishedManager()