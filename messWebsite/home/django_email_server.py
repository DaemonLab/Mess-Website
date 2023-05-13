# django-email-server.py

from django.core.mail import send_mail
from django.core import mail
from django.conf import settings

def send(subject, message, recipient):
    # send_mail(
    #     subject=subject,
    #     message=message,
    #     from_email=settings.EMAIL_HOST_USER,
    #     recipient_list=[recipient])
    with mail.get_connection() as connection:
        mail.EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient],
            connection=connection,
        ).send()
    print("Mail sent to " + recipient)



def send_html(subject, message, recipient):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient],
        html_message=message)

subject_rebate = "Short Term Rebate Application"
message_rebate ="""
Dear Student, 
Your short term rebate application from {start_date} to {end_date} has been {approved}.
"""

def rebate_mail(start_date, end_date, approved, recipient):
    subject = subject_rebate
    if(approved): message = message_rebate.format(start_date=start_date, end_date=end_date, approved = "approved")
    else: message = message_rebate.format(start_date=start_date, end_date=end_date, approved = "rejected")
    send(subject, message, recipient)

