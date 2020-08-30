from django.shortcuts import render
from .models import Mz_Post

def mz_blog_home_view(request, *args, **kwargs):
	homecontext = {
		'mzpostlist' : Mz_Post.objects.all()
	}
	return render(request, 'music/mz-blog-home.html', homecontext)