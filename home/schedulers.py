from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events

from .utils.django_email_server import __send__rebate__email__


def start():
    scheduler = BackgroundScheduler()
    if scheduler is None:
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(__send__rebate__email__, "cron", hour=23, minute=59, second=0)
        register_events(scheduler)
        scheduler.start()
        print(scheduler)
