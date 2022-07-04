from django.urls import path
from . import views
from django.conf import settings
urlpatterns = [
    path('home',views.check,name='home'),
    path('mail',views.just_mail,name='mail'),
]