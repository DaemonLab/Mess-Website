from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Student, RebateSpringSem,RebateAutumnSem, Rebate, LongRebate, TodayRebate
from .views import count
from .django_email_server import rebate_mail

__doc__="This file contains the signals for the home app"

@receiver(post_save, sender=Student)
def create_bill(sender, instance, created, **kwargs):
    if created:
        email = instance.email
        RebateAutumnSem.objects.get_or_create(email=email)
        RebateSpringSem.objects.get_or_create(email=email)
        instance.rebateautumnsem.save()
        instance.rebatespringsem.save()


def save_short_bill(email,month,days,high_tea):
    # Add  in every if else block
    print (email,month,days,high_tea)
    if month == "January":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaJanuary = high_tea
        rebate.januaryShort = rebate.januaryShort + days
        rebate.save()
    elif month == "February":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaFeburary = high_tea
        rebate.feburaryShort = rebate.februaryShort + days
        rebate.save()
    elif month == "March":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaMarch = high_tea
        rebate.marchShort = rebate.marchShort + days
        rebate.save()
    elif month == "April":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaApril = high_tea  
        rebate.aprilShort = rebate.aprilShort + days
        rebate.save()
    elif month == "May":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaMay = high_tea
        rebate.mayShort = rebate.mayShort + days
        rebate.save()
    elif month == "June":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaJune = high_tea
        rebate.juneShort = rebate.juneShort + days
        rebate.save()
    elif month == "July":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaJuly = high_tea
        rebate.julyShort = rebate.julyShort + days
        rebate.save()
    elif month == "August":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaAugust = high_tea
        rebate.augustShort = rebate.augustShort + days
        rebate.save()
    elif month == "September":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaSeptember = high_tea
        rebate.septemberShort = rebate.septemberShort + days
        rebate.save()
    elif month == "October":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaOctober = high_tea
        rebate.octoberShort = rebate.octoberShort + days
        rebate.save()
    elif month == "November":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaNovember = high_tea
        rebate.novemberShort = rebate.novemberShort + days
        rebate.save()
    elif month == "December":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaDecember = high_tea
        rebate.decemberShort = rebate.decemberShort + days
        rebate.save()

@receiver(pre_save, sender=Rebate)
def update_bill(sender, instance, **kwargs):
    print("Signal called")
    try:
        old_instance = Rebate.objects.get(pk=instance.pk)
        print(old_instance.approved,instance.approved)
        if old_instance.approved != instance.approved:
            days = count(instance.start_date, instance.end_date)
            email = instance.email
            allocation = Rebate.objects.filter(allocation_id=instance.allocation_id).last().allocation_id
            if instance.approved == True:
                save_short_bill(email,allocation.month,days,allocation.high_tea)
                new_rebate = TodayRebate(date=instance.date_applied,Caterer=allocation.caterer_name,allocation_id = allocation.student_id,start_date=instance.start_date,end_date=instance.end_date)
                new_rebate.save()
                print("Saved")
            else:
                save_short_bill(email,allocation.month,-days,allocation.high_tea)
                new_rebate = TodayRebate.objects.filter(allocation_id=allocation.student_id).last().delete()
                print("Deleted")
            rebate_mail(instance.start_date,instance.end_date,instance.approved,email)
    except Exception as e:
        print(e)

def save_long_bill(email,high_tea,days,month):
    print (email,month,days,high_tea)
    if month == "January":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaJanuary = high_tea
        rebate.januaryLong = rebate.januaryLong + days
        rebate.save()
    elif month == "February":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaFeburary = high_tea
        rebate.feburaryLong = rebate.februaryLong + days
        rebate.save()
    elif month == "March":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaMarch = high_tea
        rebate.marchLong = rebate.marchLong + days
        rebate.save()
    elif month == "April":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaApril = high_tea  
        rebate.aprilLong = rebate.aprilLong + days
        rebate.save()
    elif month == "May":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaMay = high_tea
        rebate.mayLong = rebate.mayLong + days
        rebate.save()
    elif month == "June":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaJune = high_tea
        rebate.juneLong = rebate.juneLong + days
        rebate.save()
    elif month == "July":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaJuly = high_tea
        rebate.julyLong = rebate.julyLong + days
        rebate.save()
    elif month == "August":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaAugust = high_tea
        rebate.augustLong = rebate.augustLong + days
        rebate.save()
    elif month == "September":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaSeptember = high_tea
        rebate.septemberLong = rebate.septemberLong + days
        rebate.save()
    elif month == "October":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaOctober = high_tea
        rebate.octoberLong = rebate.octoberLong + days
        rebate.save()
    elif month == "November":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaNovember = high_tea
        rebate.novemberLong = rebate.novemberLong + days
        rebate.save()
    elif month == "December":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaDecember = high_tea
        rebate.decemberLong = rebate.decemberLong + days
        rebate.save()

@receiver(pre_save, sender=LongRebate)
def update_long_bill(sender, instance, **kwargs):
    print("Signals called")
    try:
        print(instance.pk)
        old_instance = LongRebate.objects.get(pk=instance.pk)
        print("inside try")
        print(old_instance.approved,instance.approved)
        if old_instance.approved != instance.approved:
            allocation = LongRebate.objects.filter(allocation_id_id=instance.allocation_id_id).last().allocation_id_id
            email = instance.email
            if instance.approved == True:
                save_long_bill(email,allocation.high_tea,instance.days,instance.month)
            else:
                save_long_bill(email,allocation.high_tea,-instance.days,instance.month)
    except Exception as e:
        print(e)

        