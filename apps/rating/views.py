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
    return render(request, 'rating/fan.html', {'questions': questions,'category': fan} )

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
                                                          'len_javoblar': len_javoblar})
    return render(request, 'rating/tekshirish.html')

def get_dic_from_two_lists(keys, values):
    return { keys[i] : values[i] for i in range(len(keys)) }


#             print(f'Response= {response}')
#             if not response == None:
#                 for choice in choices:
#
#                     if str(choice) == response and choice.is_correct:
#                         if False not in responses:
#                             counter += 1
#                             responses.append(counter)
#                             responses.append(True)
#
#                     else:
#                         if False not in responses:
#                             counter += 1
#                             responses.append(counter)
#                             responses.append(False)
#
#
#         # responses.pop()