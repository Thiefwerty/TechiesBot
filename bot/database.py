#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
from datetime import datetime


class DatabaseManager:
    def __init__(self):
        self.changed = False
        try:
            self.df = pd.read_csv('database.csv')
        except:
            self.df = pd.DataFrame()
            self.df.to_csv('database.csv', index=False)

    def add_match(self, result):
        self.df = self.df.append({'Date': datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"), 'result': result}, ignore_index=True)
        self.changed = True

    def remove_match(self):
        self.df = self.df.iloc[:-1, :]
        self.changed = True

    def save_data(self):
        if self.changed:
            self.df.to_csv('database.csv', index=False)
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 'data saved')
        self.changed = False

    def get_stats(self, matches):
        return self.df.tail(min(int(matches), 50)).copy()

    def format_stats(self, matches):
        df = self.get_stats(matches)
        df['Time'] = df['Date'].apply(lambda x: x.split()[1])
        df['Date'] = df['Date'].apply(lambda x: x.split()[0])
        df = df[['Date', 'Time', 'result']]
        return df

    def table_print(self, matches=5):
        df = self.format_stats(matches)
        table = ''
        index = np.array([['Дата', 'Время', 'Результат']])
        df = np.vstack([index, df.values])
        part_lengths = [0] * df.shape[1]
        for i in range(df.shape[1]):
            part_lengths[i] = max(map(len, df[:, i])) + 2

        start = '╔' + '╦'.join(map(lambda x: '═' * x, part_lengths)) + '╗\n'
        delim = '╠' + '╬'.join(map(lambda x: '═' * x, part_lengths)) + '╣\n'
        end = '╚' + '╩'.join(map(lambda x: '═' * x, part_lengths)) + '╝'
        table += start
        for i in range(len(df)):
            s = '║'
            for j in range(len(df[i])):
                s += ' ' + df[i][j] + ' ' * (part_lengths[j] - len(df[i][j]) - 1) + '║'
            table += s
            table += '\n'
            if i != len(df) - 1:
                table += delim
        table += end
        return table