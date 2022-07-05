from django.shortcuts import render,redirect
from .task import test,send_mail_task,square
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def check(request):
    test.delay()
    return HttpResponse("kahatm")
def just_mail(request):
    for i in range(3):
        send_mail_task.delay()
    return HttpResponse('mail sent')
    
def demo(request):
    for i in range(3):
        square.delay()
    return HttpResponse('square')