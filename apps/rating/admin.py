from django.contrib import admin
from .models import Category, Question, Choice

admin.site.register(Category)
admin.site.register(Question)



class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice', 'question')
admin.site.register(Choice, ChoiceAdmin)

