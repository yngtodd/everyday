import os
import datetime

import numpy as np
import pandas as pd

from terminaltables import SingleTable
from everyday.cal.settings import Settings


class EverydayCalendar:

    def __init__(self, title='None', settings=Settings()):
        self.title = title
        self.settings = settings

        self.months = [
         'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ]

        self.days = np.asarray(
          [['' for x in range(12)] for y in range(31)]
        )

    def update(self):
        now = datetime.datetime.now()
        day = now.day
        month = now.month
        self.days[day-1][month-1] = '*'

    def undo_update(self):
        now = datetime.datetime.now()
        day = now.day
        month = now.month
        self.days[day-1][month-1] = ''

    def progress(self):
        data = list(self.days)
        data.insert(0, self.months)
        tab = SingleTable(data, self.title)
        tab.inner_column_border = False
        tab.inner_row_border = False
        tab.justify_columns = self.settings.justification
        print(tab.table)

    def save(self, path):
        savefile = os.path.join(path, self.title)
        df = pd.DataFrame(self.days, columns=self.months)
        df.to_csv(savefile, index=False)

    def load(self, path):
        df = pd.read_csv(path)
        self.days = df.values
