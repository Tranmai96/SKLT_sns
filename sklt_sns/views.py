from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    posts=Post.objects.order_by('-created_date')
    latest_posts = []
    for i in range(6):
        latest_posts.append(posts[i])

    context={'posts':posts,'latest_posts':latest_posts}
    return render(request, 'sklt_sns/home.html',context)

def post_detail(request):
    return HttpResponse('Post detail')

def profile(request):
    return HttpResponse('Profile')

def search_result(request):
    return HttpResponse('Search result')

def log_in_page(request):
    return HttpResponse('Log in page')


