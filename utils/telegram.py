from __future__ import absolute_import

import time
import requests
import datetime

from main.models import Order


class Telegram:
    def __init__(self, url, token, channel_id, message):
        self.token = token
        self.url = url.format(self.token)
        self.chanel_id = channel_id
        self.message = message

    def send_message(self, id):
        try:
            r = requests.post(self.url, data={'chat_id': self.chanel_id,
                                              'text': self.message.format(id)})
            if r.status_code == '200':
                return True
            else:
                return r.status_code
        except Exception as ex:
            print(ex)

    @staticmethod
    def get_all_orders():
        orders = Order.objects.all()
        return orders

    def send_messages(self):
        for order in self.get_all_orders():
            if order.deadline < datetime.date.today():
                time.sleep(3)
                self.send_message(order.order_number)


