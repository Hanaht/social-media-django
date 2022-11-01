from django.urls import path
from django.urls import include, re_path
from articles.views import searchh,image_upload_view

from .views import (
ArticleListView,
ArticleUpdateView,
ArticleDetailView,
ArticleCreateView,
ArticleDeleteView, 
AddLike,
AddDislike,
)
urlpatterns = [
path('<int:pk>/edit/',
ArticleUpdateView.as_view(), name='article_edit'), # new
path('<int:pk>/',
ArticleDetailView.as_view(), name='article_detail'), # new
path('<int:pk>/delete/',
ArticleDeleteView.as_view(), name='article_delete'), # new
path('like/<int:pk>/', AddLike.as_view(), name='like'),
path('dislike/<int:pk>/', AddDislike.as_view(), name='dislike'),
path('new/', ArticleCreateView.as_view(), name='article_new'),
path('', ArticleListView.as_view(), name='article_list'),
re_path(r'^searchh/', searchh, name='searchh'),
]