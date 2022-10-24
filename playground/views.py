from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Here we can create request and will return a response
# It is a request handler

def say_hello(request):
    return render(request, 'hello.html', {'name': 'Mosh'})