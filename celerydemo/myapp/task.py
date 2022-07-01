from celery import shared_task
from celery import Celery
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def test():
    for i in range(10):
        print(i)
    return "done"
@shared_task(blind = True)
def send_mail_task():
    users = get_user_model().objects.all()
    print(users)
    for user in users:
        mail_subject = "hi! celery"
        message = "this is demo mail for django celery"
        to_mail = user.email
        # send_mail(
        #     subject = mail_subject,
        #     message = message,
        #     from_mail = "drashtij59@gmail.com",
        #     recipient_list = [to_mail],
        #     fail_silently = True,
        # )
        send_mail(
            'DB testing',
            ' bla bla bla !!!!',
            'drashtij59@gmail.com',
            [to_mail],
            fail_silently = True,
        )

        print(to_mail,"skhjkjhashadhs")
        return "yo i got mail"