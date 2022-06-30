from django.shortcuts import render,redirect
from .task import test
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def check(request):
    test.delay()
    return HttpResponse("done")