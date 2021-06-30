from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import *


def home(request):
    categories = Category.objects.all()
    return render(request, 'rating/home.html', {'categories': categories})


def fan(request, id):
    fan = Category.objects.get(id=id)
    questions = fan.question_set.all()
    return render(request, 'rating/fan.html', {'questions': questions, 'category': fan})


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
def add_category(request):
    cate_form = CategoryForm()
    if request.method == "POST":
        cate_form = CategoryForm(request.POST)
        if cate_form.is_valid():
            fan = cate_form.save()
            return HttpResponseRedirect(reverse('add_new_question', args=(fan.id,)))

    return render(request, 'rating/add_category.html', {'cate_form': cate_form})



@login_required
def add_new_question(request, id):
    fan = Category.objects.get(id=id)
    ques_form = QuestionForm(initial={'category': fan})
    if request.method == "POST":
        ques_form = QuestionForm(request.POST, initial={'category': fan})
        if ques_form.is_valid():
            new_ques = ques_form.save()
            return HttpResponseRedirect(reverse('add_new_choice', args=(fan.id, new_ques.id,)))

    return render(request, 'rating/add_question.html', {'ques_form': ques_form, 'category': fan})


@login_required
def add_new_choice(request, id, pk):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    choice_form = AddChoiceForm(initial={'question': question})
    if request.method == "POST":
        choice_form = AddChoiceForm(request.POST, initial={'question': question})
        if choice_form.is_valid():
            choice_form.save()
        return HttpResponseRedirect(reverse('fan', args=(fan.id,)))

    return render(request, 'rating/add_choice.html', {'choice_form': choice_form, 'category': fan,
                                                      'question': question,
                                                      })




@login_required
def edit_question(request, id, pk):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    ques_form = QuestionForm(instance=question)
    if request.method == "POST":
        ques_form = QuestionForm(request.POST, instance=question)
        if ques_form.is_valid():
            ques_form.save()
            return HttpResponseRedirect(reverse('fan', args=(fan.id,)))
    return render(request, 'rating/edit_question.html', {'ques_form': ques_form,
                                                         'category': fan,
                                                         'question': question,
                                                         })


@login_required
def edit_question_text(request, id, pk, p):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    choice = question.choice_set.get(id=p)
    choice_form = ChoiceForm(instance=choice)
    if request.method == "POST":
        choice_form = ChoiceForm(request.POST, instance=choice)
        if choice_form.is_valid():
            choice_form.save()
        return HttpResponseRedirect(reverse('fan', args=(fan.id,)))

    return render(request, 'rating/edit_question_text.html', {'choice_form': choice_form, 'category': fan,
                                                              'question': question,
                                                              'choice': choice})


@login_required
def delete_category(request, id):
    fan = Category.objects.get(id=id)
    if request.method == "POST":
        fan.delete()
        return redirect('/')

    return render(request, 'rating/delete_category.html', {'category': fan,
                                                           })



@login_required
def delete_question(request, id, pk):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    if request.method == "POST":
        question.delete()
        return HttpResponseRedirect(reverse('fan', args=(fan.id,)))

    return render(request, 'rating/delete_question.html', {'category': fan,
                                                           'question': question,
                                                           })



@login_required
def delete_question_text(request, id, pk, p):
    fan = Category.objects.get(id=id)
    question = fan.question_set.get(id=pk)
    choice = question.choice_set.get(id=p)
    if request.method == "POST":
        choice.delete()
        return HttpResponseRedirect(reverse('fan', args=(fan.id,)))

    return render(request, 'rating/delete_question_text.html', {'category': fan,
                                                                'question': question,
                                                                'choice': choice})

