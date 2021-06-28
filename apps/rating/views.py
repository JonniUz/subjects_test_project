from logging import exception

from django.shortcuts import render, redirect
from .models import Category, Choice, Question
from django.http import HttpResponse

def home(request):
    categories = Category.objects.all()
    return render(request, 'rating/home.html', {'categories': categories})


def fan(request, id):
    fan = Category.objects.get(id=id)
    questions = fan.question_set.all()
    return render(request, 'rating/fan.html', {'questions': questions} )

def tekshirish(request):
    responses = []
    counter = 0
    questions = Question.objects.all()
    if request.method == "POST":
        for question in questions:
            choices = question.choice_set.all()
            response = request.POST.get(f'{question.id}')
            print(f'Response= {response}')
            if not response == None:
                for choice in choices:

                    if str(choice) == response and choice.is_correct:
                        if False not in responses:
                            counter += 1
                            responses.append(counter)
                            responses.append(True)

                        list = convert(responses)
                    else:
                        if False not in responses:
                            counter += 1
                            responses.append(counter)
                            responses.append(False)
                        list = convert(responses)


        # responses.pop()

        return render(request, 'rating/tekshirish.html', {'list': list})
    return render(request, 'rating/tekshirish.html')


def convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}

    return res_dct
