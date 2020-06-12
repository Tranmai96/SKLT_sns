from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post_detail',views.post_detail),
    path('profile',views.profile),
    path('log_in_page',views.log_in_page),

]