from .models import Task
from django.forms import ModelForm,TextInput,Textarea
class TaskForm(ModelForm):
    class Meta:
        model= Task
        fields =["title","task"]
        vidgets ={"title":Textarea(attrs={
                'placeholder': 'Введите текст',
                'class': 'form-control'}),
                  
                "task":Textarea(attrs={
                'placeholder': 'Введите текст',
                'class': 'form-control'})
        }
        
        