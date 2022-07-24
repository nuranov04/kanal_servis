import gspread

from datetime import datetime

from main.models import Order
from utils.script import get_rate


class GoogleSheet:
    """
    class for work with Google sheet's api
    """

    def __init__(self, google_sheet_name: str, worksheet_name: str, column_name: str):
        self.column_name = column_name
        self.service_account = gspread.service_account()
        self.sh = self.service_account.open(google_sheet_name)
        self.ks = self.sh.worksheet(worksheet_name)

    def get_all_values_from_google_sheet(self):
        """
        method for getting all fields from Google worksheet

        :return: List[List[...], List[...], ...] or empty List
        """
        values = self.ks.get_all_values()
        values.pop(0)  # remove first value in list, because values[0] is names of columns
        return values

    def set_to_db(self):
        """
        method for create or update fields in db
        :return: 'ok' or exception
        """
        try:
            rows = self.get_all_values_from_google_sheet()  # getting all fields from Google worksheet
            rate = get_rate('USD')  # getting currency
            for i in rows:  # iteration on list
                deadline = datetime.strptime(i[3], '%d.%m.%Y')  # formatting str to date
                """
                update_or_create need for update or create in db
                if it's row in db -> update
                if it's row not in db -> create
                :return False if updated
                :return True is created
                """
                Order.objects.update_or_create(id=int(i[0]), order_number=int(i[1]),
                                               defaults={'amount_dollar': int(i[2]),
                                                         'amount_rub': int(rate * int(i[2])),
                                                         'deadline': deadline,
                                                         })
            return 'ok'
        except Exception as ex:
            print('error', ex)
            return ex
