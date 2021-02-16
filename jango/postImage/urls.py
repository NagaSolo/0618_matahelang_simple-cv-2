from django.urls import path

from . import views

urlpatterns = [
    path('', views.rumah, name='postImage-rumah'),
    path('tentang/', views.tentang, name='postImage-tentang'),
]