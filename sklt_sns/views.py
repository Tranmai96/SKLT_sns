from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
# Create your views here.

def home(request):
    return render(request, 'sklt_sns/main.html')

def post_detail(request):
    return HttpResponse('Post detail')

def log_in_page(request):
    return HttpResponse('Log in page')

#投稿一覧
def profile(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'sklt_sns/profile.html',context)

#各投稿の個別ページ
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'SKLT_sns/post_detail.html', {'post': post})

#新規投稿画面
@login_required
def post_new(request):
    
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'SKLT_sns/post_edit.html', {'form': form})

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

#下書き一覧
@login_required
def post_draft_list(request):
    
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'SKLT_sns/post_draft_list.html', {'posts': posts})

#投稿する
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

#削除する
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

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
    return render(request, 'SKLT_sns/add_comment_to_post.html', {'form': form})

#コメントを公開
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

#コメントを削除
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def search_result(request):
    return HttpResponse('Search result')


