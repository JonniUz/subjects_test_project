from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('tekshirish/<int:id>/', views.tekshirish, name='tekshirish'),
    path('tests/<int:id>/', views.fan, name='fan'),

    path('edit_question/<int:id>/<int:pk>/', views.edit_question, name='edit_question'),
    path('edit_question_text/<int:id>/<int:pk>/<int:p>/', views.edit_question_text, name='edit_question_text'),

    path('delete_question/<int:id>/', views.delete_category, name='delete_category'),
    path('delete_question/<int:id>/<int:pk>/', views.delete_question, name='delete_question'),
    path('delete_question_text/<int:id>/<int:pk>/<int:p>/', views.delete_question_text, name='delete_question_text'),

    path('add_category', views.add_category, name='add_category'),
    path('add_new_question/<int:id>/', views.add_new_question, name='add_new_question'),
    path('add_new_choice/<int:id>/<int:pk>/', views.add_new_choice, name='add_new_choice'),
]

