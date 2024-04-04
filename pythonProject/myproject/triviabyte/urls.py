from django.urls import path
from . import views
from .views import get_quiz

urlpatterns = [
    path('', views.triviabyte_view, name='triviabyte_view'),
    path('api/quiz/', views.get_quiz, name='get_quiz'),
    path('submit_answers/', views.submit_answers, name='submit_answers')
    path('music.html', views.music_view, name='music'),
    path('science.html', views.science_view, name='science'),
    path('quiz.html', views.quiz_view, name='quiz'),
]