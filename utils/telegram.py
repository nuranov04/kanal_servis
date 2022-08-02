from __future__ import absolute_import

import time
import requests
import datetime

from main.models import Order


class Telegram:
    """
    class for send messages to telegram
    """

    def __init__(self, url, token, channel_id, message):
        self.token = token
        self.url = url.format(self.token)
        self.chanel_id = channel_id
        self.message = message

    def send_message(self, id):
        """
        method for send message

        :param id: number_order
        :return: status_code ot exception
        """
        try:
            r = requests.post(self.url, data={'chat_id': self.chanel_id,
                                              'text': self.message.format(id)})
            return r.status_code
        except Exception as ex:
            print(ex)

    @staticmethod
    def get_all_orders():
        """
        method for get all records from table
        :return: object_Class
        """
        return Order.objects.all()

    def send_messages(self):
        """
        method get all_records from table and validate deadline
        if deadline > to day send message to telegram
        :return: None
        """
        for order in self.get_all_orders():
            if order.deadline < datetime.date.today():
                time.sleep(3)
                self.send_message(order.order_number)
