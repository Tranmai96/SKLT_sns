from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    posts = Post.objects.order_by('-created_date')
    keyword = request.GET.get('keyword')
    latest_posts = []
    if keyword:
        posts1 = posts.filter(
                 Q(text__icontains=keyword) | Q(author__name__icontains=keyword)
               )
        for i in posts1:
            latest_posts.append(i)
        
        messages.success(request, '「{}」の検索結果'.format(keyword))
    else:
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



