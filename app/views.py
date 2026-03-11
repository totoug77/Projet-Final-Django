from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todolist
from .forms import NoteForm

@login_required # Oblige à être connecté pour voir l'accueil
def home(request):
    return render(request, 'index.html')

@login_required
def note(request):
    if request.method == "POST":
        designation = request.POST.get('designation')
        if designation:
            Todolist.objects.create(designation=designation)
            return redirect('note')
    notes = Todolist.objects.all()
    return render(request, 'app/note.html', {'notes': notes})

@login_required
def delete_note(request, note_id):
    item = get_object_or_404(Todolist, id=note_id)
    item.delete()
    return redirect('note')

# --- NOUVELLE FONCTION MODIFIER ---
@login_required
def update_note(request, pk):
    note_obj = get_object_or_404(Todolist, id=pk)
    form = NoteForm(instance=note_obj)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note_obj)
        if form.is_valid():
            form.save()
            return redirect('note')
    return render(request, 'app/update_note.html', {'form': form})