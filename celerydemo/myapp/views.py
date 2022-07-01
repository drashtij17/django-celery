from django.shortcuts import render,redirect
from .task import test,send_mail_task
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def check(request):
    test.delay()
    return HttpResponse("kahatm")
def just_mail(request):
    send_mail_task.delay()
    print("wormi")
    return HttpResponse('mail sent')