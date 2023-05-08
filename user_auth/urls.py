from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('', views.user_login, name='login'),
    path('authenticate_user/user/', views.show_user, name='show_user'),
    path('authenticate_user/', views.authenticate_user, name='authenticate_user'),
    path('new_user/', views.new_user, name="new_user"),
    path('user_logout', views.user_logout, name="logout"),
]