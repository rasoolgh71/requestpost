from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'task/home.html')
def send(request):
    return render(request,'task/send.html')
