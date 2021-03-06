from django.db import models
from django.urls import reverse
import re
from django import forms
from django.conf import settings

KIND_CHOICES = (
    ('이슈공유','first'),
    ('장애발생','second'),
    ('이력관리','third'),
    ('기타','fourth'),
)

class Post(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default='이슈공유')
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    auto_increment_id = models.ForeignKey(Post, on_delete=models.PROTECT)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=20)