from tempfile import tempdir
from celery import shared_task
from celery import Celery
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def test():
    return None
# def user_details():
#     users = get_user_model().objects.all()
#     return users
@shared_task(blind = True)
def send_mail_task():
    users = get_user_model().objects.all()
        
    for user in users:
        print(user.email,"jjjjj")
        mail_subject = "hi! celery"
        message = "this is demo mail for django celery asdhashdjas"
        to_mail = user.email
        print("@#@@@@@",to_mail)
        # send_mail(
        #     subject = mail_subject,
        #     message = message,
        #     from_mail = "drashtij59@gmail.com",
        #     recipient_list = [to_mail],
        #     fail_silently = True,
        # )
        send_mail(
            'DB testing',
            ' It is break time',
            'drashtij59@gmail.com',
            [to_mail],
            fail_silently = True,
        )
        print("line---36")
        print(to_mail,"skhjkjhashadhs")
    return "notification"
    
@shared_task(blind = True)
def square():
    l1=[]
    for i in range(800):
        l1.append(i**i)
    return l1
