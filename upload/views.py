from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages

from .forms import DocumentForm
from .models import Document


def UploadView(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            messages.success(request, 'File uploaded successfully !!!')
        return HttpResponseRedirect('/upload')
    else:
        form = DocumentForm()

    try:
        documents = Document.objects.all()
    except Document.DoesNotExist:
        documents = None
    return render(request, 'consultation/upload.html', {'documents': documents, 'form': form})

def CreateViewWork(request):
    try:
        documents = Document.objects.all()
    except Document.DoesNotExist:
        documents = None
    return render(request, 'consultation/index.html', {'documents': documents})
