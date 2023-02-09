from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('schedule/', schedule_controller, name='schedule'),
    path('wiki/', wiki_controller, name='wiki'),
    path('categories/', categories_controller, name='categories'),
    path('form/', AddParticipantView.as_view(), name='form'),
]