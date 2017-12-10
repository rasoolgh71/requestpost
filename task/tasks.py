import string
#from django.contrib.auth.models import User
from .models import Message
from django.utils.crypto import get_random_string
from django.shortcuts import HttpResponse
from celery import shared_task

@shared_task
def create_random_user_accounts(num):
    list=[]
    for i in range(num):
        message = get_random_string(8)
        #list.append(message)
        new_message=Message(message=message)
        new_message.save()
    return '{} random users created with success!'.format(num)