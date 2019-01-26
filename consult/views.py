from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.core.mail import send_mail

from .forms import ConsultForm


def book(request):
    if request.method == 'POST':
        form = ConsultForm(request.POST)

        if form.is_valid():
           form.save()

           messages.success(request, 'Form successfully submitted !!!')
        return HttpResponseRedirect('/consult')
        
    else:
        form = ConsultForm()
        context = {
            'form': form
        }
        
    return render(request, 'consult/consult.html', context)

