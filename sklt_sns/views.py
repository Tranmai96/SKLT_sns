from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'sklt_sns/home.html')

def post_detail(request):
    return HttpResponse('Post detail')

def profile(request):
    return HttpResponse('Profile')

def search_result(request):
    return HttpResponse('Search result')

def log_in_page(request):
    return HttpResponse('Log in page')


