import logging
from datetime import datetime

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import (
    Allocation,
    Caterer,
    CatererBills,
    LongRebate,
    Period,
    Rebate,
    Semester,
    Student,
    StudentBills,
    UnregisteredStudent,
)
from .utils.django_email_server import long_rebate_mail, rebate_mail
from .utils.month import fill_periods
from .utils.rebate_bills_saver import save_long_bill, save_short_bill
from .utils.rebate_checker import count

__doc__ = "This file contains the signals for the home app"
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@receiver(post_save, sender=Student)
def create_bill(sender, instance, created, **kwargs):
    if created:
        semester = Semester.objects.filter().last()
        rebate_bill, _ = StudentBills.objects.get_or_create(
            email=instance, semester=semester
        )
        rebate_bill.save()


@receiver(post_save, sender=Rebate)
def direct_update_bill(sender, instance: Rebate, created, **kwargs):
    logger.info("Signal called for Creating Short Rebate")
    try:
        if created:
            student = instance.email
            allocation = instance.allocation_id
            start_date = instance.start_date
            end_date = instance.end_date
            days = count(start_date, end_date)
            save_short_bill(
                student,
                allocation.period,
                days,
                allocation.high_tea,
                allocation.caterer,
            )
            rebate_mail(
                instance.start_date, instance.end_date, instance.approved, student.email
            )
            logger.info("Saved")
        else:
            logger.info("Not Created")
    except Exception as e:
        logger.error(e)


@receiver(pre_save, sender=Rebate)
def update_short_bill(sender, instance: Rebate, **kwargs):
    logger.info("Signal called for Updating Short Rebate")
    try:
        old_instance = Rebate.objects.filter(pk=instance.pk).first()
        if old_instance is None:
            return
        if old_instance.approved != instance.approved:
            email = instance.email
            allocation = instance.allocation_id
            start_date = instance.start_date
            end_date = instance.end_date
            days = count(start_date, end_date)
            if days < 0:
                raise ValueError("Days are negative")
            print(old_instance.approved, instance.approved)
            if instance.approved is True:
                save_short_bill(
                    email,
                    allocation.period,
                    days,
                    allocation.high_tea,
                    allocation.caterer,
                )
                logger.info("Saved")
            else:
                save_short_bill(
                    email,
                    allocation.period,
                    -days,
                    allocation.high_tea,
                    allocation.caterer,
                )
                logger.info("Deleted")
            rebate_mail(
                instance.start_date, instance.end_date, instance.approved, email.email
            )
    except Exception as e:
        logger.error(e)


@receiver(pre_save, sender=LongRebate)
def update_long_bill(sender, instance: LongRebate, **kwargs):
    logger.info("Signal called for Updating Long Rebate")
    try:
        old_instance = LongRebate.objects.filter(pk=instance.pk).first()
        if old_instance is None:
            return
        logger.info(f"Approved: {instance.approved}, Reason: {instance.reason}")
        if (
            old_instance.approved != instance.approved
            or old_instance.reason != instance.reason
        ):
            email = instance.email
            days_per_period = fill_periods(
                email, instance.start_date, instance.end_date
            )
            left_start_date = [
                period
                for period, days in days_per_period
                if isinstance(period, type(days))
            ]
            left_end_date = [
                days
                for period, days in days_per_period
                if isinstance(period, type(days))
            ]

            if instance.approved is True:
                save_long_bill(email, days_per_period, 1)
                long_rebate_mail(
                    instance.start_date,
                    instance.end_date,
                    instance.approved,
                    email.email,
                    left_start_date,
                    left_end_date,
                    instance.reason,
                )
            elif instance.approved is False:
                save_long_bill(email, days_per_period, -1)
                long_rebate_mail(
                    instance.start_date,
                    instance.end_date,
                    instance.approved,
                    email.email,
                    left_start_date,
                    left_end_date,
                    instance.reason,
                )
    except Exception as e:
        logger.error(e)


@receiver(post_save, sender=Allocation)
def update_rebate_bill(sender, instance: Allocation, created, **kwargs):
    try:
        if created:
            sno = instance.period.Sno
            days = (instance.period.end_date - instance.period.start_date).days + 1
            high_tea = instance.high_tea
            rebate_bill, _ = StudentBills.objects.get_or_create(
                email=instance.email, semester=instance.period.semester
            )
            amount = 115
            # if(high_tea):
            #     amount=130
            if sno == 1:
                rebate_bill.period1_high_tea = high_tea
                rebate_bill.period1_bill = amount * days
            elif sno == 2:
                rebate_bill.period2_high_tea = high_tea
                rebate_bill.period2_bill = amount * days
            elif sno == 3:
                rebate_bill.period3_high_tea = high_tea
                rebate_bill.period3_bill = amount * days
            elif sno == 4:
                rebate_bill.period4_high_tea = high_tea
                rebate_bill.period4_bill = amount * days
            elif sno == 5:
                rebate_bill.period5_high_tea = high_tea
                rebate_bill.period5_bill = amount * days
            elif sno == 6:
                rebate_bill.period6_high_tea = high_tea
                rebate_bill.period6_bill = amount * days
            rebate_bill.save()
    except Exception as e:
        logger.error(e)


@receiver(post_save, sender=Period)
def create_unregistered(sender, instance, created, **kwargs):
    if created:
        for student in Student.objects.all():
            unregistered, _ = UnregisteredStudent.objects.get_or_create(
                email=str(student.email)
            )
            unregistered.period = instance
            unregistered.save()


@receiver(post_save, sender=Semester)
def create_catererBills(sender, instance, created, **kwargs):
    if created:
        for caterer in Caterer.objects.filter(visible=True).all():
            caterer_bill, _ = CatererBills.objects.get_or_create(
                caterer=caterer, semester=instance
            )
            caterer_bill.save()


@receiver(post_save, sender=Caterer)
def create_catererBills(sender, instance, created, **kwargs):
    logger.info("Caterer created: %s", instance.name)
    if created:
        for semester in Semester.objects.all():
            end_date = (
                Period.objects.filter(semester=semester)
                .order_by("end_date")
                .last()
                .end_date
            )
            if end_date and end_date < datetime.now().date():
                continue
            caterer_bill, _ = CatererBills.objects.get_or_create(
                caterer=instance, semester=semester
            )
            caterer_bill.save()
