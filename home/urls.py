from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login.html/', views.login, name='login'),
    path('user-order-track.html', views.user_order_track, name='user_order_track'),
]
