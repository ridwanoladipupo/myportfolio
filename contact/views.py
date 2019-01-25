from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .forms import ContactForm


def contactme(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
           form.save()

           messages.success(request, 'Form successfully submitted !!!')
        return HttpResponseRedirect('/contact')

    else:
        form = ContactForm()
        
    return render(request, 'contact/contact.html', {'form': form})
