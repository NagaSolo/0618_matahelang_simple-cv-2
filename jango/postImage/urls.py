from django.urls import path

from . import views

# class list view
from .views import (
    ImejListView, 
    ImejDetailView,
    ImejCreateView
)

urlpatterns = [
    # path('', views.rumah, name='postImage-rumah'),
    path('', ImejListView.as_view(), name='postImage-rumah'),
    path('imej/<int:pk>/', ImejDetailView.as_view(), name='postImage-detail'),
    path('imej/baru/', ImejCreateView.as_view(), name='postImage-create'),
    path('tentang/', views.tentang, name='postImage-tentang'),
]