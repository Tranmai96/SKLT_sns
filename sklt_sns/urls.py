from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('log_in_page',views.log_in_page),
    path('post_detail',views.post_detail),
    path('profile/',views.profile),
    #各記事の個別ページ
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    #コメント投稿
    path('post_detail/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #いいね
    path('good/<int:pk>', views.good, name='good'),
    #編集
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #削除
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]
 