# quiz/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('api/start/', views.start_quiz, name='start_quiz'),
    path('api/start_session/', views.start_session, name='start_session'),
    path('api/question/', views.get_random_question, name='get_random_question'),
    path('api/submit/', views.submit_answer, name='submit_answer'),
    path('api/results/', views.results, name='results'),
]

