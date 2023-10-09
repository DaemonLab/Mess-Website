# django-email-server.py
from ..models.students import TodayRebate
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

message_long_rebate = """
Dear Student,
Your long term rebate application from {start_date} to {end_date} has been {approved}.
Bills for them have been {added} your account.
"""
left_message = """Note: Bills for {left_start_date} to {left_end_date} will be removed as an when you are allotcated a caterer during this period.
"""

def rebate_mail(start_date, end_date, approved, recipient):
    subject = subject_rebate
    if(approved): message = message_rebate.format(start_date=start_date, end_date=end_date, approved = "approved")
    else: message = message_rebate.format(start_date=start_date, end_date=end_date, approved = "rejected")
    send(subject, message, recipient)

def caterer_mail(message,name,recipient,date_applied):
    subject = "Caterer Mail Rebate Mail"
    message = htmlUp.format(name=name,date=date_applied) +message + htmlBottom
    send_html(subject, message, recipient)

def long_rebate_mail(start_date, end_date, approved, recipient, left_start_date, left_end_date):
    subject = "Long Term Rebate Application"
    if(approved): 
        message = message_long_rebate.format(start_date=start_date, end_date=end_date, approved = "approved",added="removed from")
        if(left_start_date != None):
            message += left_message.format(left_start_date=left_start_date, left_end_date=left_end_date)
    else: 
        message = message_long_rebate.format(start_date=start_date, end_date=end_date, approved = "rejected",added="added to")
    send(subject, message, recipient)

def __send__rebate__email__():
    from datetime import date
    today = date.today()
    queryset = TodayRebate.objects.filter(date=today)
    text = "<li> {name} with {allocation_id} has applied from {start_date} to {end_date}</li>"
    messageKanaka=""
    messageGauri=""
    messageAjay=""
    date = today
    for obj in queryset:
        allocation=obj.allocation_id
        if(obj.Caterer == "Kanaka"):
            messageKanaka +=(text.format(allocation_id=allocation.student_id,name=allocation.email.name, start_date=obj.start_date, end_date=obj.end_date))
        elif(obj.Caterer == "Gauri"):
            messageGauri +=(text.format(allocation_id=allocation.student_id,name=allocation.email.name, start_date=obj.start_date, end_date=obj.end_date))
        elif(obj.Caterer == "Ajay"):
            messageAjay +=(text.format(allocation_id=allocation.student_id,name=allocation.email.name, start_date=obj.start_date, end_date=obj.end_date))
        obj.delete()
    print(messageKanaka)
    print(messageGauri)
    print(messageAjay)
    if(messageAjay): caterer_mail(messageAjay, "Ajay","mems220005054@iiti.ac.in", date)
    if(messageKanaka): caterer_mail(messageKanaka, "Kanaka","mems220005054@iiti.ac.in",date)
    if(messageGauri): caterer_mail(messageGauri, "Gauri","mems220005054@iiti.ac.in",date)
    return

