from django.shortcuts import render,HttpResponse,HttpResponseRedirect
import string
from .models import Message
from django.utils.crypto import get_random_string
from celery import Celery
from celery import shared_task
from django.conf import settings
#app=Celery('twoscoops')
#app.autodiscover_tasks()
# Create your views here.
app = Celery('task', broker='amqp://guest@localhost//')


def home(request):
    return render(request,'task/home.html')

def show(request):
    return render(request,'task/show.html')

@shared_task()
def send(request):
    list=[]
    if request.method =="POST":
        num = request.POST.get('num')
        for i in range(int(num)):
            message = get_random_string(8)
            list.append(message)
            #print('list :',i,message)
        return render(request, 'task/show.html',context={'list':list,'num':num})
    return render(request,'task/send.html')
