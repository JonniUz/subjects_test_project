from django import forms

from .models import Category, Choice, Question


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"
