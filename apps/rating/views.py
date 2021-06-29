from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.forms.formsets import formset_factory
from .models import Category
from .forms import *


def home(request):
    categories = Category.objects.all()
    return render(request, 'rating/home.html', {'categories': categories})


@login_required
def fan(request, id):
    fan = Category.objects.get(id=id)
    questions = fan.question_set.all()
    return render(request, 'rating/fan.html', {'questions': questions, 'category': fan})


@login_required
def tekshirish(request, id):
    tartib = []
    javoblar = []
    correct_answer_count = 0
    counter = 0
    fan = Category.objects.get(id=id)
    questions = fan.question_set.all()
    if request.method == "POST":
        for question in questions:
            choices = question.choice_set.all()
            response = request.POST.get(f'{question.id}')
            counter += 1
            if not response == None:
                for choice in choices:
                    if str(choice) == response:
                        if choice.is_correct:
                            tartib.append(counter)
                            javoblar.append(True)
                            # responses.append(counter)
                            # responses.append(True)
                            correct_answer_count += 1
                            break
                        else:
                            tartib.append(counter)
                            javoblar.append(False)
                            # responses.append(counter)
                            # responses.append(False)
                            break

        respon = get_dic_from_two_lists(tartib, javoblar)
        len_javoblar = len(javoblar)
        len_questions = len(questions)
        return render(request, 'rating/tekshirish.html', {'correct_answer_count': correct_answer_count,
                                                          'respon': respon,
                                                          'len_questions': len_questions,
                                                          'len_javoblar': len_javoblar,
                                                          'category': fan})
    return render(request, 'rating/tekshirish.html')


def get_dic_from_two_lists(keys, values):
    return {keys[i]: values[i] for i in range(len(keys))}











@login_required
def add_new_question(request):
    ques_form = QuestionForm()
    if request.method=="POST":
        ques_form = QuestionForm(request.POST)
        if ques_form.is_valid():
            ques_form.save()
            return HttpResponseRedirect(reverse('add_new_choice'))

    return render(request, 'rating/add_question.html', {'ques_form': ques_form})


@login_required
def add_new_choice(request, id=0):
    choice_form = ChoiceForm()
    if request.method=="POST":
        choice_form = ChoiceForm(request.POST)
        if choice_form.is_valid():
            choice_form.save()
            choice_form.full_clean()
    return render(request, 'rating/add_choice.html', {'choice_form': choice_form})









@login_required
def edit_question(request, id, pk):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    ques_form = QuestionForm(instance=question)
    if request.method=="POST":
        ques_form = QuestionForm(request.POST, instance=question)
        if ques_form.is_valid():
            ques_form.save()
            return HttpResponseRedirect(reverse('fan', args=(fan.id,)))
    return render(request, 'rating/edit_question.html', {'ques_form': ques_form,
                                                         'category': fan,
                                                         'question': question
                                                         })


@login_required
def edit_question_text(request, id, pk, p):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    choice = question.choice_set.get(id=p)
    choice_form = ChoiceForm(instance=choice)
    if request.method=="POST":
        choice_form = ChoiceForm(request.POST, instance=choice)
        if choice_form.is_valid():
            choice_form.save()
        return HttpResponseRedirect(reverse('fan', args=(fan.id,)))


    return render(request, 'rating/edit_question_text.html', {'choice_form': choice_form,'category': fan,
                                                              'question': question,
                                                              'choice': choice})




def add(request):
    ChoiceFormSet = formset_factory(ChoiceForm, extra=3, min_num=2, validate_min=True)
    if request.method == "POST":
        form = QuestionForm(request.POST)
        formset = ChoiceFormSet(request.POST)
        if all([form.is_valid()]):
            question = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    choice = inline_form.save(commit=False)
                    choice.question = question
                    choice.save()
                    return redirect('home')
                return render(request, 'rating/add.html', {})
        else:
            form = QuestionForm()
            formset = ChoiceFormSet()
        return render(request, 'rating/add.html', {'form': form,'formset': formset})

def add_new(request, id, pk, p):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    choice = question.choice_set.get(id=p)
    if request.method=="POST":
        ques_form = QuestionForm(request.POST, instance=question)
        choice_form = ChoiceForm(request.POST, instance=choice)
        if ques_form.is_valid():
            question = ques_form.save(commit=False)

            choice = choice_form.save(False)
            choice.question = question
            choice.save()
    ques_form = QuestionForm()
    choice_form = ChoiceForm()
    context = {'ques_form': ques_form, 'choice_form': choice_form}
    return render(request, 'rating/add_new.html', context)