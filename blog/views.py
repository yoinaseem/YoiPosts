from django.shortcuts import render
from .models import Post 
from django.views.generic.detail import DetailView 

def home_view(request, *args, **kwargs):
	return render(request, 'blog/home.html')

def cs_blog_home_view(request, *args, **kwargs):
	homecontext = {
		'postlist' : Post.objects.all()
	}
	return render(request, 'blog/cs-blog-home.html', homecontext)

def about_view(request, *args, **kwargs):
	return render(request, 'blog/about.html', {'title':'About'})

