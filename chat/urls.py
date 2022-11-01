from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("searchh/", views.searchh, name="searchh"),
    path("addfriend/<str:name>", views.addFriend, name="addFriend"),
    path("chat/<str:username>", views.chat, name="chat"),
    path('api/messages/<int:sender>/<int:receiver>', views.message_list, name='message-detail'),
    path('api/messages', views.message_list, name='message-list'),
]
