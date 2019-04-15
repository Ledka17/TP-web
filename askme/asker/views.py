from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator
from faker import Faker
# Здесь хранятся функиии, которые рендерят конкретную страницу из шаблонов

fake = Faker()
questions_ = []
for i in range(1, 20):
    questions_.append({
        'title': fake.sentence(),
        'id': i,
        'text': fake.text(),
        'rating': fake.random_int() % 50,
        'answers': fake.random_int() % 20,
        'tags': ['C++', 'Python'],
    })
for i in range(20, 40):
    questions_.append({
        'title': fake.sentence(),
        'id': i,
        'text': fake.text(),
        'rating': fake.random_int() % 50,
        'answers': fake.random_int() % 20,
        'tags': ['Technopark'],
    })


def questions(request):  # Главная страница
    return render_with_paginate(request, 'questions.html', questions_, {
        'questions': questions_,
    })


def login(request):  # Форма логина
    return render(request, 'auth.html', {
        'questions': questions_,
    })


def hot(request):  # Список лучших вопросов (20 штук)
    hot_questions = sorted(questions_, key=lambda k: k['rating'], reverse=True)
    return render_with_paginate(request, 'hot_questions.html', hot_questions[:20], {
        'questions': hot_questions[:20]
    })


def signup(request):  # Форма регистрации
    return render(request, 'signup.html', {})


def ask(request):  # Форма создания вопроса
    return render(request, 'ask.html', {})


def question(request, qid):  # Страница одного конкретного вопроса
    answers_ = []
    for i in range(int(questions_[qid - 1]['answers'])):
        answers_.append({
            'title': fake.sentence(),
            'id': i,
            'text': fake.text(),
            'rating': fake.random_int() % 50,
            'tags': ['C++', 'Python'],
        })
    return render_with_paginate(request, 'question.html', answers_, {
        'question': questions_[qid - 1],
        'answers': answers_,
    })


def tag(request, qtag):  # Список вопросов по тегу
    tag_questions = [i for i in questions_ if qtag in i['tags']]
    return render_with_paginate(request, 'tag_questions.html', tag_questions, {
        'qtag': qtag,
        'questions': tag_questions,
    })


def settings(request, name):  # Настройки пользователя
    return render(request, 'settings.html', {
        'name': name,
    })


def paginate(request, objects_list):  # Функиция пагинации
    paginator = Paginator(objects_list, 10)  # Показывать по 10 объектов на странице
    page = request.GET.get('page')
    object_page = paginator.get_page(page)
    return object_page, paginator


def render_with_paginate(request, url, object_list, dict_to_paginate):
    obj_list, paginator = paginate(request, object_list)
    dict_to_paginate.update({
        'objects_list': obj_list,
        'paginator': paginator,
    })
    return render(request, url, dict_to_paginate)