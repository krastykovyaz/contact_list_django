from django.shortcuts import render

from django.http import HttpResponse
from .models import Contact

def index(request):
    return HttpResponse('Hello')

#display all the objects from the table
def display(request):
    contacts = Contact.objects.all() 

    s = ''
    for c in contacts:
        s += c.to_string() + '<br>'
    return HttpResponse("Contacts:<br>" + s)