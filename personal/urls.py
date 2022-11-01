from django.urls import path, include
from . import views

from .views import HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]