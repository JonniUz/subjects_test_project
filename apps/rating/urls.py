from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tekshirish/<int:id>/', views.tekshirish, name='tekshirish'),
    path('tests/<int:id>/', views.fan, name='fan'),
]
