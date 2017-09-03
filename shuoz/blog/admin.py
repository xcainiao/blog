# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from markdownx.admin import MarkdownxModelAdmin
from blog.models import blog,  ImagePost

# Register your models here.
class ProjectImageInline(admin.StackedInline):
    model = ImagePost

class BlogPostClass(admin.ModelAdmin):
    inlines = [ProjectImageInline, ]

admin.site.register(blog, BlogPostClass)
