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
    ('완료', '완료'),
    ('진행', '진행'),
    ('보류', '보류'),
)

class Post(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    is_status = models.CharField(max_length=7, choices=IS_STATUS, default='ing')
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default='first')
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