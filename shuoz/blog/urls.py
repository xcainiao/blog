from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/(?P<post_name>.+)$', views.content, name='content'),
    url(r'^about/$', views.about, name='about'),
    url(r'^links/$', views.links, name='links'),
]
