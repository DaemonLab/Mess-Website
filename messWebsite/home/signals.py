from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Student, RebateSpringSem,RebateAutumnSem, Rebate, LongRebate, TodayRebate, CatererBillsAutumn, CatererBillsSpring, Caterer
from .views import count
from .utils.django_email_server import rebate_mail
from .utils.month import fill_days

__doc__="This file contains the signals for the home app"

@receiver(post_save, sender=Student)
def create_bill(sender, instance, created, **kwargs):
    if created:
        rebate_autumn_sem, _ =RebateAutumnSem.objects.get_or_create(email=instance)
        rebate_spring_sem, _ =RebateSpringSem.objects.get_or_create(email=instance)
        rebate_autumn_sem.save()
        rebate_spring_sem.save()


def save_short_bill(email,month,days,high_tea, caterer):
    # Add  in every if else block
    caterer = Caterer.objects.get(name=caterer)
    amount = days*115
    if(high_tea):
        amount = amount + days*15
    print (email,month,days,high_tea, caterer)
    if month == "January":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaJanuary = high_tea
        rebate.januaryShort = rebate.januaryShort + days
        rebate.save()
        catererBill = CatererBillsSpring.objects.get(Caterer=caterer)
        catererBill.januaryBill = catererBill.januaryBill + amount
        catererBill.save()
    elif month == "February":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaFeburary = high_tea
        rebate.feburaryShort = rebate.februaryShort + days
        rebate.save()
        catererBill = CatererBillsSpring.objects.get(Caterer=caterer)
        catererBill.feburaryBill = catererBill.feburaryBill + amount
        catererBill.save()
    elif month == "March":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaMarch = high_tea
        rebate.marchShort = rebate.marchShort + days
        rebate.save()
        catererBill = CatererBillsSpring.objects.get(Caterer=caterer)
        catererBill.marchBill = catererBill.marchBill + amount
        catererBill.save()
    elif month == "April":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaApril = high_tea  
        rebate.aprilShort = rebate.aprilShort + days
        rebate.save()
        catererBill = CatererBillsSpring.objects.get(Caterer=caterer)
        catererBill.aprilBill = catererBill.aprilBill + amount
        catererBill.save()
    elif month == "May":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaMay = high_tea
        rebate.mayShort = rebate.mayShort + days
        rebate.save()
        catererBill = CatererBillsSpring.objects.get(Caterer=caterer)
        catererBill.mayBill = catererBill.mayBill + amount
        catererBill.save()
    elif month == "June":
        rebate = RebateSpringSem.objects.get(email=email)
        rebate.highTeaJune = high_tea
        rebate.juneShort = rebate.juneShort + days
        rebate.save()
        catererBill = CatererBillsSpring.objects.get(Caterer=caterer)
        catererBill.juneBill = catererBill.juneBill + amount
        catererBill.save()
    elif month == "July":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaJuly = high_tea
        rebate.julyShort = rebate.julyShort + days
        rebate.save()
        catererBill = CatererBillsAutumn.objects.get(Caterer=caterer)
        catererBill.julyBill = catererBill.julyBill + amount
        catererBill.save()
    elif month == "August":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaAugust = high_tea
        rebate.augustShort = rebate.augustShort + days
        rebate.save()
        catererBill = CatererBillsAutumn.objects.get(Caterer=caterer)
        catererBill.augustBill = catererBill.augustBill + amount
        catererBill.save()
    elif month == "September":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaSeptember = high_tea
        rebate.septemberShort = rebate.septemberShort + days
        rebate.save()
        catererBill = CatererBillsAutumn.objects.get(caterer=caterer)
        catererBill.septemberBill = catererBill.septemberBill + amount
        catererBill.save()
    elif month == "October":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaOctober = high_tea
        rebate.octoberShort = rebate.octoberShort + days
        rebate.save()
        catererBill = CatererBillsAutumn.objects.get(caterer=caterer)
        catererBill.octoberBill = catererBill.octoberBill + amount
        catererBill.save()
    elif month == "November":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaNovember = high_tea
        rebate.novemberShort = rebate.novemberShort + days
        rebate.save()
        catererBill = CatererBillsAutumn.objects.get(caterer=caterer)
        catererBill.novemberBill = catererBill.novemberBill + amount
        catererBill.save()
    elif month == "December":
        rebate = RebateAutumnSem.objects.get(email=email)
        rebate.highTeaDecember = high_tea
        rebate.decemberShort = rebate.decemberShort + days
        rebate.save()
        catererBill = CatererBillsAutumn.objects.get(caterer=caterer)
        catererBill.decemberBill = catererBill.decemberBill + amount
        catererBill.save()

@receiver(pre_save, sender=Rebate)
def update_bill(sender, instance, **kwargs):
    print("Signal called for Short Rebate")
    try:
        old_instance = Rebate.objects.get(pk=instance.pk)
        print(old_instance.approved,instance.approved)
        if old_instance.approved != instance.approved:
            days = count(instance.start_date, instance.end_date)
            email = instance.email
            allocation = Rebate.objects.filter(allocation_id=instance.allocation_id).last().allocation_id
            if instance.approved == True:
                save_short_bill(email,allocation.month,days,allocation.high_tea, allocation.caterer_name)
                new_rebate = TodayRebate(date=instance.date_applied,Caterer=allocation.caterer_name,allocation_id = allocation.student_id,start_date=instance.start_date,end_date=instance.end_date)
                new_rebate.save()
                print("Saved")
            else:
                save_short_bill(email,allocation.month,-days,allocation.high_tea, allocation.caterer_name)
                new_rebate = TodayRebate.objects.filter(allocation_id=allocation.student_id).last().delete()
                print("Deleted")
            rebate_mail(instance.start_date,instance.end_date,instance.approved,email)
    except Exception as e:
        print(e)

def save_long_bill(email,days_per_month,j):
    print (email,days_per_month,j)
    for month, days in days_per_month:
        days = int(days)*j
        if month == "January":
            rebate = RebateSpringSem.objects.get(email=email)
            rebate.januaryLong = rebate.januaryLong + days
            rebate.save()
        elif month == "February":
            rebate = RebateSpringSem.objects.get(email=email)
            rebate.feburaryLong = rebate.februaryLong + days
            rebate.save()
        elif month == "March":
            rebate = RebateSpringSem.objects.get(email=email)
            rebate.marchLong = rebate.marchLong + days
            rebate.save()
        elif month == "April":
            rebate = RebateSpringSem.objects.get(email=email)
            rebate.aprilLong = rebate.aprilLong + days
            rebate.save()
        elif month == "May":
            rebate = RebateSpringSem.objects.get(email=email)
            rebate.mayLong = rebate.mayLong + days
            rebate.save()
        elif month == "June":
            rebate = RebateSpringSem.objects.get(email=email)
            rebate.juneLong = rebate.juneLong + days
            rebate.save()
        elif month == "July":
            rebate = RebateAutumnSem.objects.get(email=email)
            rebate.julyLong = rebate.julyLong + days
            rebate.save()
        elif month == "August":
            rebate = RebateAutumnSem.objects.get(email=email)
            rebate.augustLong = rebate.augustLong + days
            rebate.save()
        elif month == "September":
            rebate = RebateAutumnSem.objects.get(email=email)
            rebate.septemberLong = rebate.septemberLong + days
            rebate.save()
        elif month == "October":
            rebate = RebateAutumnSem.objects.get(email=email)
            rebate.octoberLong = rebate.octoberLong + days
            rebate.save()
        elif month == "November":
            rebate = RebateAutumnSem.objects.get(email=email)
            rebate.novemberLong = rebate.novemberLong + days
            rebate.save()
        elif month == "December":
            rebate = RebateAutumnSem.objects.get(email=email)
            rebate.decemberLong = rebate.decemberLong + days
            rebate.save()

@receiver(pre_save, sender=LongRebate)
def update_long_bill(sender, instance, **kwargs):
    print("Signals called for long rebate")
    try:
        print(instance.pk)
        old_instance = LongRebate.objects.get(pk=instance.pk)
        print("inside try")
        print(old_instance.approved,instance.approved)
        if old_instance.approved != instance.approved:
            email = instance.email
            days_per_month = fill_days(instance.start_date, instance.end_date)
            if instance.approved == True:
                save_long_bill(email,days_per_month,1)
            else:
                save_long_bill(email,days_per_month,-1)
    except Exception as e:
        print(e)

        