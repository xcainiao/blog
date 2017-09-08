# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

from markdownx.models import MarkdownxField

# Create your models here.
class blog(models.Model):
    CHOICES = (
            ('programming','Programming'),
            ('nc', 'No'),
        )
    article = models.CharField(max_length=152, blank=True)
    title = models.CharField(max_length=152, blank=True)
    category = models.CharField(max_length=30, choices=CHOICES, blank=True)
    file = models.FileField(upload_to='content/%Y/%m/', blank=True)
    date = models.DateTimeField('date', default = timezone.now)
    edit = models.DateTimeField('date', default = timezone.now)
    
    class Meta:    
        ordering = ['-date']

class ImagePost(models.Model):
    imgid = models.ForeignKey(blog, related_name='img')
    img = models.ImageField(upload_to='img/%Y/%m/', blank=True)
    
