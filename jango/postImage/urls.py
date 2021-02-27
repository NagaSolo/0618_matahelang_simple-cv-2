from django.urls import path

from . import views

# class list view
from .views import (
    ImejListView, 
    ImejDetailView,
    ImejCreateView,
    ImejUpdateView,
    ImejDeleteView
)

urlpatterns = [
    # path('', views.rumah, name='postImage-rumah'),
    path('', ImejListView.as_view(), name='postImage-rumah'),
    path('imej/<int:pk>/', ImejDetailView.as_view(), name='postImage-detail'),
    path('imej/baru/', ImejCreateView.as_view(), name='postImage-create'),
    path('imej/<int:pk>/kemaskini/', ImejUpdateView.as_view(), name='postImage-update'),
    path('imej/<int:pk>/buang/', ImejDeleteView.as_view(), name='postImage-delete'),
    path('tentang/', views.tentang, name='postImage-tentang'),
]