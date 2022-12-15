import pandas as pd
import numpy as np
import datetime as dt


def reduce_mem_usage(df, list_col_category=['col_4', ]):
    """ Трансформация типов данных колонок датафрейма для оптимизации потребления памяти """
    start_mem = df.memory_usage().sum() / 1024 ** 2
    print('Потребление памяти до оптимизации {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype.name
        if col_type[:3] == 'int':
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
        elif col_type[:5] == 'float':
            if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                df[col] = df[col].astype(np.float16)
            elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                df[col] = df[col].astype(np.float32)
            else:
                df[col] = df[col].astype(np.float64)
        elif col_type == 'timestamp':
            df[col] = pd.to_datetime(df[col])
        elif (col_type == 'object') and (col in list_col_category):
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024 ** 2
    print('Потребление памяти после оптимизации: {:.2f} MB'.format(end_mem))
    print('Разница {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df


parser = lambda date: dt.datetime.strptime(date, '%d.%m.%Y')
df_test = pd.read_csv('./data.csv', parse_dates=['col_5'], date_parser=parser, decimal=',')

reduce_mem_usage(df_test)
