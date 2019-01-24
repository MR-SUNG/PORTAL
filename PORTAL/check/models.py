from django.db import models
from django.urls import reverse
import re
from django import forms
from django.conf import settings

KIND_CHOICES = (
    ('이슈공유', '이슈공유'),
    ('장애이력', '장애이력'),
    ('이력관리', '이력관리'),
    ('기타', '기타'),
)

IS_STATUS = (
    ('진행', '진행'),
    ('완료', '완료'),
)

class Post(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    is_status = models.CharField(max_length=7, choices=IS_STATUS, default='진행')
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default='이슈공유')
    content = models.TextField(max_length=1000)
    tags = models.ManyToManyField('Tag')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-auto_increment_id']


class Comment(models.Model):
    auto_increment_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-create_at']

    def get_auto_increment_id(self):
        return reverse('check:index', args=[self.post.pk, self.pk])


class Tag(models.Model):
    name = models.CharField(max_length=20)