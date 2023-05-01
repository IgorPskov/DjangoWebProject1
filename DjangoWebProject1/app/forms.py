"""
Definition of forms.
"""
from django.db import models
from .models import Comment
from .models import Blog

from cProfile import label
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class Feedback(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=100)
    birth = forms.DateField(label='Дата рождения')
    gender = forms.ChoiceField(label='Ваш пол', choices=[('1', 'Мужской'), ("2", "Женский")], widget=forms.RadioSelect, initial=1)
    using = forms.ChoiceField(label='Пользуетесь ли Вы другими ресурсами, содержащими новости автомобильного мира?', 
            choices=[('1', 'Да, часто'), ('2', 'Да, иногда'), ('3', 'Нет')], widget = forms.RadioSelect, initial=1)
    auto = forms.ChoiceField(label='Имеете ли Вы свой собственный автомобиль?', choices=[('1', 'Да'), ('2', 'Нет')], widget = forms.RadioSelect, initial=1)
    mark_info = forms.ChoiceField(label = 'Как бы Вы оценили информативность сайта по пятибальной шкале?', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    mark_comfort = forms.ChoiceField(label = 'Как бы Вы оценили удобство сайта по пятибальной шкале?', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    mark_design = forms.ChoiceField(label = 'Как бы Вы оценили дизайн сайта по пятибальной шкале?', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    mark_func = forms.ChoiceField(label = 'Как бы Вы оценили функционал сайта по пятибальной шкале?', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
    wish = forms.CharField(label = 'Напишите, пожалуйста, Ваши пожелания по улучшению сайта', widget=forms.Textarea(attrs={'rows': 12, 'cols': 100}))
    notice = forms.BooleanField(label = 'Хотели бы Вы получать уведомления о свежих новостях на вашу электронную почту?', required = False)
    email = forms.EmailField(label = 'Ваш e-mail', min_length=7)

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}







       

