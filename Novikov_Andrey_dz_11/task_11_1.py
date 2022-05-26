import re
from datetime import datetime


class Date:

    RE_DATE = re.compile(r'^(\d{2}-){2}\d{4}$')

    def __init__(self, str_date):
        if Date.check_correctness_date(str_date):
            self.str_date = str_date

    @classmethod
    def get_parts_date(cls, str_date):
        date = datetime.strptime(str_date, '%d-%m-%Y').date()
        return {'day': date.day, 'month': date.month, 'year': date.year}

    @staticmethod
    def check_correctness_date(str_date):
        match = Date.RE_DATE.match(str_date)
        if match is None:
            print('Invalid date format')
            return False
        try:
            Date.get_parts_date(str_date)
        except ValueError as err:
            print(err)
            return False
        return True


data_1 = Date('01-02-2022')
data_2 = Date('30-00-2022')
print(data_1.get_parts_date(data_1.str_date))
