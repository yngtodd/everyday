import time


class EverydayCalendar:

    def __init__(self):
        self.dates = {
            'Jan': ['' for x in range(31)],
            'Feb': ['' for x in range(31)],
            'Mar': ['' for x in range(31)],
            'Apr': ['' for x in range(31)],
            'May': ['' for x in range(31)],
            'Jun': ['' for x in range(31)],
            'Jul': ['' for x in range(31)],
            'Aug': ['' for x in range(31)],
            'Sep': ['' for x in range(31)],
            'Oct': ['' for x in range(31)],
            'Nov': ['' for x in range(31)],
            'Dec': ['' for x in range(31)]
        }

    def update(self):
        day = time.strftime("%d")
        month = time.strftime("%b")
        self.dates[month][day] = '*'

    def get_table(self):
        header = list(self.dates.keys())
