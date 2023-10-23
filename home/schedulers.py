from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.schedulers.background import BackgroundScheduler
from .utils.django_email_server import __send__rebate__email__
import sys, socket

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("127.0.0.1", 47200))
except socket.error:
    print, "!!!scheduler already started, DO NOTHING"
else:
    def start():
        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")
        scheduler.add_job(__send__rebate__email__, 'cron', hour=23, minute=59, second=0)
        register_events(scheduler) 
        scheduler.start()
        print, "scheduler started"
