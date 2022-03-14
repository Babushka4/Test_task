from django.urls import path
from . import views


urlpatterns = [
            path('', views.main_window, name='home'),
            path('all_fulls/', views.show_all_fulls, name='show_all_fulls')
            ]