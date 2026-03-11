from django import forms
from .models import Todolist

class NoteForm(forms.ModelForm):
    class Meta:
        model = Todolist
        fields = ['designation'] # Le champ que l'on veut modifier