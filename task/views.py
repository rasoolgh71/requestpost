from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib import messages
import subprocess
import os
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from .forms import GenerateRandomUserForm
from .models import Message
from .tasks import create_random_user_accounts


def home(request):
    return render(request,'task/home.html')

def show(request):
    return render(request, 'task/show.html')

class MessageListView(ListView):  # show list of random mesage
    template_name = 'task/show.html'
    model = Message
    context_object_name = 'latest_list'

    def get_queryset(self):
         return Message.objects.all()

class GenerateRandomMessageView(FormView):   # craete work celry and random message
    template_name = 'task/send.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        num = form.cleaned_data.get('num')
        create_random_user_accounts.delay(num)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('show')

def is_disk(request):    # show volumn-name- modify date directory
    list=[]
    dict={}
    data={}
    #disk = subprocess.Popen(["ls", "-l"],stdout=subprocess.PIPE, shell=True)
   # disk = disk.communicate()
    process = subprocess.Popen(["ls -l  |  awk  '{ print $5,$6 $8 $7 , $9 }'"], cwd='/home/parspooyesh-kashan/test-1',
                              stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
    disk,err = process.communicate()
    disk=disk.decode('utf-8').split('\n')
    #disk = disk.decode('utf-8')
    #disk1=[disk.strip() for n in disk]
    #disk1=[disk.split() for n in disk]

    #list=list.append(disk)
    for i in disk:
        data[i]=i.split(' ')
        print(data[i])
        #data.pop()

        #print(type(dict1))

       # print(data)
        print("data:",data)
        #pass

    #lits1=list.split('\n')
    return render(request,'task/disk.html',context={'disk':disk,'data':data})