from .models import Articles, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    """ArticlesForm: Articles - это название модели в models.py"""
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'tag']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
             "tag": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Теги'
            }),
        }


class CommentForm(ModelForm):
    """ArticlesForm: Articles - это название модели в models.py"""
    class Meta:
        model = Comments
        fields = ['text',]

        widgets = {
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий',
                'rows': 5,
                
            }),

        }