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
answers_ = []
    for i in range(int(questions_[qid - 1]['answers'])):
        answers_.append({
            'title': fake.sentence(),
            'id': i,
            'text': fake.text(),
            'rating': fake.random_int() % 50,
            'tags': ['C++', 'Python'],
        })


def questions(request):  # Главная страница
    obj_list, paginator = paginate(request, questions_)
    return render(request, 'questions.html', {
        'questions': questions_,
        'objects_list': obj_list,
        'paginator': paginator,
    })


def login(request):  # Форма логина
    return render(request, 'auth.html', {
        'questions': questions_,
    })


def hot(request):  # Список лучших вопросов (20 штук)
    hot_questions = sorted(questions_, key=lambda k: k['rating'], reverse=True)
    obj_list, paginator = paginate(request, hot_questions[:20])
    return render(request, 'hot_questions.html', {
        'questions': hot_questions[:20],
        'objects_list': obj_list,
        'paginator': paginator,
    })


def signup(request):  # Форма регистрации
    return render(request, 'signup.html', {})


def ask(request):  # Форма создания вопроса
    return render(request, 'ask.html', {})


def question(request, qid):  # Страница одного конкретного вопроса
    obj_list, paginator = paginate(request, answers_)
    return render(request, 'question.html', {
        'question': questions_[qid - 1],
        'answers': answers_,
        'objects_list': obj_list,
        'paginator': paginator,
    })


def tag(request, qtag):  # Список вопросов по тегу
    tag_questions = [i for i in questions_ if qtag in i['tags']]
    obj_list, paginator = paginate(request, tag_questions)
    return render(request, 'tag_questions.html', {
        'qtag': qtag,
        'questions': tag_questions,
        'objects_list': obj_list,
        'paginator': paginator,
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


#def render_with_paginate(request, object_list):
#    obj_list, paginator = paginate(request, object_list)
#    return render(request, 'tag_questions.html', {
#        'qtag': qtag,
#        'questions': object_list,
#        'objects_list': obj_list,
#        'paginator': paginator,
#    })