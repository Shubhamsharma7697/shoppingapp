from django.shortcuts import render,HttpResponse

# Create your views 

def home(request):
    return HttpResponse("hello")