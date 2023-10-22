from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/home/', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('login/home/delete/<int:video_id>/', views.delete_video, name='delete_video'),
    path('login/home/like/<int:video_id>/', views.increment_like, name='increment_likes'),
    path('login/home/comment/<int:video_id>/', views.add_comment, name='add_comment'),
]