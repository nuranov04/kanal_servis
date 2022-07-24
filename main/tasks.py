from celery.utils.log import get_task_logger

from utils.google_sheet import GoogleSheet
from utils.telegram import Telegram
from test_for_company_kanalservise.celery import app
from conf_file import *

logger = get_task_logger(__name__)


@app.task
def update_or_create_order():
    """
    task for create or update records
    """
    google_sheet = GoogleSheet(google_sheet_name, worksheet_name, column_name)
    google_sheet.set_to_db()
    logger.info(f"created or update")


@app.task
def send_message():
    """
    task for send messages to telegram
    :return:
    """
    telegram = Telegram(url, token, channel_id, message)
    telegram.send_messages()
    logger.info('send messages')
