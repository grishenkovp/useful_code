import pandas as pd
import numpy as np
import datetime as dt

parser = lambda date: dt.datetime.strptime(date, '%d.%m.%Y')
df_test = pd.read_csv('./data.csv', parse_dates=['col_5'], date_parser=parser, decimal=',')

def IQR_for_column(df:pd.DataFrame, col_name:str):
    """ Функция возвращает квартили, выводит границы для выбросов, согласно IQR и
    считает сколько выбросов (в том числе в %)"""
    perc25 = df[col_name].quantile(0.25)
    perc75 = df[col_name].quantile(0.75)
    IQR = perc75 - perc25
    min_out = perc25 - 1.5*IQR
    max_out = perc75 + 1.5*IQR
    anomaly = len(df[df[col_name] > max_out]) + \
        len(df[df[col_name] < min_out])
    print(
        '25-й перцентиль: {} |'.format(perc25),
        '75-й перцентиль: {} |'.format(perc75),
        "IQR: {} | ".format(IQR),
        "Границы выбросов: [{}, {}].".format(min_out, max_out))
    print("Выбросов, согласно IQR: {} | {:2.2%}".format(
        anomaly, anomaly/len(df)))

IQR_for_column(df_test,'col_1')
