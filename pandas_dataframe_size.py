import pandas as pd
import numpy as np
import datetime as dt

parser = lambda date: dt.datetime.strptime(date, '%d.%m.%Y')
df_test = pd.read_csv('./data.csv', parse_dates=['col_5'], date_parser=parser, decimal=',')


def num_bytes_format(num_bytes, float_prec=4):
    """ Вывод объема памяти, который занимает датафрейм """
    units = ['bytes', 'Kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb']
    for unit in units[:-1]:
        if abs(num_bytes) < 1000:
            return f'{num_bytes:.{float_prec}f} {unit}'
        num_bytes /= 1000
    return f'{num_bytes:.4f} {units[-1]}'

num_bytes = df_test.memory_usage(deep=True).sum()
print(num_bytes_format(num_bytes))
