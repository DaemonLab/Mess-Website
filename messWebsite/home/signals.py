from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Student, Rebate, LongRebate, TodayRebate, CatererBillsAutumn, CatererBillsSpring, Caterer, RebateAutumn22, RebateAutumn23, RebateSpring23
from .utils.rebate_checker import count
from .utils.django_email_server import rebate_mail
from .utils.month import fill_periods
from .utils.rebate_bills_saver import save_short_bill, save_long_bill

__doc__="This file contains the signals for the home app"

@receiver(post_save, sender=Student)
def create_bill(sender, instance, created, **kwargs):
    if created:
        rebate_autumn_sem, _ =RebateAutumn23.objects.get_or_create(email=instance)
        rebate_spring_sem, _ =RebateSpring23.objects.get_or_create(email=instance)
        rebate_autumn_sem.save()
        rebate_spring_sem.save()


@receiver(pre_save, sender=Rebate)
def update_short_bill(sender, instance, **kwargs):
    print("Signal called for Short Rebate")
    try:
        old_instance = Rebate.objects.get(pk=instance.pk)
        print(old_instance.approved,instance.approved)
        if old_instance.approved != instance.approved:
            days = count(instance.start_date, instance.end_date)
            email = instance.email
            allocation = instance.allocation_id
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


@receiver(pre_save, sender=LongRebate)
def update_long_bill(sender, instance, **kwargs):
    print("Signals called for long rebate")
    try:
        old_instance = LongRebate.objects.get(pk=instance.pk)
        print("inside try")
        print(old_instance.approved,instance.approved)
        if old_instance.approved != instance.approved:
            email = instance.email
            days_per_period = fill_periods(instance.start_date, instance.end_date)
            if instance.approved == True:
                save_long_bill(email,days_per_period,1)
            else:
                save_long_bill(email,days_per_period,-1)
    except Exception as e:
        print(e)

        