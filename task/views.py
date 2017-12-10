from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
import string
from django.contrib import messages
from django.utils.crypto import get_random_string
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
    return render(request,'task/show.html')

class UsersListView(ListView):
    template_name = 'task/show.html'
    model = Message
    context_object_name ='latest_list'

    def get_queryset(self):
         return Message.objects.all()

class GenerateRandomUserView(FormView):
    template_name = 'task/send.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        num = form.cleaned_data.get('num')
        create_random_user_accounts.delay(num)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        #return render(self.request, 'task/show.html', context={'list': list, 'num': num})
        return redirect('show')
