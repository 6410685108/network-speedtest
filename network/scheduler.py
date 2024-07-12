from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

def start():
    if not settings.DEBUG:
        from .views import test_internet_speed
        scheduler = BackgroundScheduler()
        scheduler.add_job(test_internet_speed, 'interval', minutes=5)
        scheduler.start()
