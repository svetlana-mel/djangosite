from django import forms
from .models import Participants

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participants
        fields = ('fname', 'lname', 'email', 'event', 'age', 'groups', 'types')
        # присваиваем стили полям формы
        widgets = {
            'event': forms.Select(), 
            'groups': forms.CheckboxSelectMultiple(),
            'types': forms.CheckboxSelectMultiple(),
        }

        labels = {
            'fname': 'Имя',
            'lname': 'Фамилия', 
            'email': 'Адрес электронной почты', 
            'event': 'Выберите соревнование', 
            'types': 'Ваша группа', 
            'age': 'Ваша возрастная группа', 
            'groups': 'Ваш разряд',
        }

        # placeholder = {
        #     'fname': 'Введите ваше имя',
        #     'lname': 'Введите вашу фамилию',
        #     'email': 'Введите email ...',
        # }