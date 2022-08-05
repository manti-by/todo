from django.shortcuts import render

from notes.forms import AddNoteForm


def index(request):
    notes = []
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            # Create new DB record
            pass
    else:
        form = AddNoteForm()
    return render(request, "index.html", {"notes": notes, "form": form})

