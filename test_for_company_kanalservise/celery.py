from __future__ import absolute_import

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_for_company_kanalservise.settings')
app = Celery('test_for_company_kanalservise', broker='redis://127.0.0.1:6379')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app.conf.beat_schedule = {
    'update-create-every-5-minutes': {  # создание таска создание или обновления заказа каждые 5 минут
        'task': 'main.tasks.update_or_create_order',
        'schedule': 360,
    },
    'send_messages': {  # отправка сообщения о пропущенном дедлайне  в телеграмм группу
        'task': 'main.tasks.send_message',
        'schedule': 4800
    }
}
app.conf.timezone = 'Asia/Bishkek'
