from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, I am Charles Raja R")

def home(request):
    return HttpResponse("Home")