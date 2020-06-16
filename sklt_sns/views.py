from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.db.models import Q
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
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

#投稿一覧
def profile(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'sklt_sns/profile.html',context)

#各投稿の個別ページ
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'SKLT_sns/post_detail.html', {'post': post})

#投稿の編集ページ
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'SKLT_sns/post_edit.html', {'form': form})

#削除する
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('profile')


#投稿に対するコメント投稿
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'SKLT_sns/post_detail.html', {'form': form})

#いいね
def good(request, pk):
    """いいねボタンをクリック."""
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # データの新規追加
        post.good += 1
        post.save()
    return redirect('post_detail', pk=post.pk)


def search_result(request):
    return HttpResponse('Search result')

def log_in_page(request):
    return HttpResponse('Log in page')



