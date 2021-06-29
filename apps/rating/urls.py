from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tekshirish/<int:id>/', views.tekshirish, name='tekshirish'),
    path('tests/<int:id>/', views.fan, name='fan'),
    path('edit_question/<int:id>/<int:pk>/', views.edit_question, name='edit_question'),
    path('edit_question_text/<int:id>/<int:pk>/<int:p>/', views.edit_question_text, name='edit_question_text'),
    path('add_new_question/', views.add_new_question, name='add_new_question'),
    path('add_new_choice/', views.add_new_choice, name='add_new_choice'),
    path('add/', views.add, name='add'),
    path('add_new/<int:id>/<int:pk>/<int:p>/', views.add_new, name='add_new'),
]
