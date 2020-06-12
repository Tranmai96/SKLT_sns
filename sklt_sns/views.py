from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
# Create your views here.

def home(request):
    return render(request, 'sklt_sns/main.html')

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


def add_ine(request, pk):

    post = get_object_or_404(Post, pk=pk)
    ip_address = get_client_ip(request)
    ips = [ine.ip_address for ine in Ine.objects.filter(parent=post).all()]

    if request.method == 'POST':
        if ip_address in ips:
            msg = '登録済みです'
        else:
            ine = Ine.objects.create(ip_address=ip_address, parent=post)
            ine.save()
            msg = '登録しました'
        d = {
            'count': Ine.objects.filter(parent=post).count(),
            'msg': msg,
        }
        return JsonResponse(d)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

