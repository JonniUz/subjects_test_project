from django import forms

from .models import Category, Choice, Question


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {
            'name': 'Category Name'
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"

        labels = {
            'category': 'Category Name',
            'text': 'Question'
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice', 'is_correct')


class AddChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"

        labels = {
            'choice': 'Variant'
        }
