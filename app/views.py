from django.shortcuts import render, redirect, get_object_or_404
from .models import Todolist

def note(request):
    if request.method == "POST":
        designation = request.POST.get('designation')
        if designation:
            Todolist.objects.create(designation=designation)
        return redirect('note')

    notes = Todolist.objects.all()
    return render(request, 'app/note.html', {'notes': notes})

def delete_note(request, note_id):
    item = get_object_or_404(Todolist, id=note_id)
    item.delete()
    return redirect('note')
def home(request):
    return render(request, 'index.html')