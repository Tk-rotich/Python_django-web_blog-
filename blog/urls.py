from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import post
 
urlpatterns = [ url(r'^$',ListView.as_view(queryset=post.objects.all().order_by("-date")[:25],template_name="blog/blog.html"))]

# Create your views here.
