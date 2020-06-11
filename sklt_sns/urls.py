from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post_detail',views.post_detail),
    path('profile/',views.profile),
    path('search_result',views.search_result),
    path('log_in_page',views.log_in_page),
    #各記事の個別ページ
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #新規投稿
    path('post/new/', views.post_new, name='post_new'),
    #編集
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #下書き
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    #投稿
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #削除
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    #コメント投稿
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #コメント公開
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    #コメント削除
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

]
 