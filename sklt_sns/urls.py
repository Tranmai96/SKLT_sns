from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('post_detail',views.post_detail),
    path('profile',views.profile),
    path('search_result',views.search_result),
    path('log_in_page',views.log_in_page),

]
 