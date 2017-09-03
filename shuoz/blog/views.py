# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, Http404

from markdownx.utils import markdownify

from blog.models import blog

import locale
import sys
import os
# Create your views here.

def index(request):
    try:
        p = blog.objects.all()
    except:
        return HttpResponse("<h1>something error</h1>")
    return render(request, "index.html", {'blogposts': p}) 

def content(request, post_name):
    html = "404"
    post = dict()
    try:
        p = blog.objects.get(title=post_name)
    except:
        return HttpResponse("<h1>file does not exist</h1>")
    post['title'] = post_name
    filename = os.path.join("/usr/src/app/upload", str(p.file))
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read()
    except:
        return HttpResponse("<h1>file does not exist</h1>")
    post['content'] = markdownify(content)
    post['date'] = p.date
    return render(request, "content.html", {'post': post}) 
