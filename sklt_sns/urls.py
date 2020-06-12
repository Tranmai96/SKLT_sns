from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post_detail',views.post_detail),
    path('profile/',views.profile),
    path('log_in_page',views.log_in_page),
    #各記事の個別ページ
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    #コメント投稿
    path('post_detail/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('post_detail/<int:pk>/ine_ajax/', views.add_ine, name='ine'),  

]
 