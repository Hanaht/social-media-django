
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.views.generic.base import TemplateView
from articles.views import searchh,image_upload_view
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path



from registration.views import (
    register_view,
    login_view,
    logout_view,
    account_search_view,

)
from chat.views import searchh

urlpatterns = [
  #  path('', home_screen_view, name='home'),
    path('account/', include('registration.urls', namespace='account')),
    path('admin/', admin.site.urls),
    path('friend/', include('friend.urls', namespace='friend')),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
    path('search/', account_search_view, name="search"),
   path('articles/', include('articles.urls')),
    path("searchh/", searchh, name="searchh"),
    path('', include('personal.urls')),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'),
         name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'),
         name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
         name='password_reset_complete'),
             path("", include("django.contrib.auth.urls")),
             path("", include("chat.urls")),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
