# django-email-server.py

from django.core.mail import send_mail
from django.core import mail
from django.conf import settings

def send(subject, message, recipient):
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
    print("Mail sent to " + recipient)

subject_rebate = "Short Term Rebate Application"
message_rebate ="""
Dear Student, 
Your short term rebate application from {start_date} to {end_date} has been {approved}.
"""
htmlUp = """\
<html>
  <body>
    <p>Dear {name} Caterer,<br>
         <h3>Following is the list of students who have applied for rebate on {date}:</h3>
       <ul>
       """
htmlBottom = """\
         </ul>
    </p>
  </body>
</html>"""
def rebate_mail(start_date, end_date, approved, recipient):
    subject = subject_rebate
    if(approved): message = message_rebate.format(start_date=start_date, end_date=end_date, approved = "approved")
    else: message = message_rebate.format(start_date=start_date, end_date=end_date, approved = "rejected")
    send(subject, message, recipient)

def caterer_mail(message,name,recipient,date_applied):
    subject = "Caterer Mail Rebate Mail"
    message = htmlUp.format(name=name,date=date_applied) +message + htmlBottom
    send_html(subject, message, recipient)


