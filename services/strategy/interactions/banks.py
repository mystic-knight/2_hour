
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from datetime import datetime, timedelta
from dateutil import relativedelta

import yfinance as yf

def months_to_timedelta(months):
    days_in_month = 30  # Assuming an average of 30 days in a month
    days = months * days_in_month
    return timedelta(days=days)

def banks(invested_amount = 100000, months = 4):
    response = {'status': False}
    current_probables = ['SBIN.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 'KOTAKBANK.NS', 'AXISBANK.NS']

    df = pd.DataFrame()
    for s in current_probables:
        df[s] = yf.download(s,period='2y')['Adj Close']

    d1 = datetime.now()
    d2 = datetime.now() + months_to_timedelta(months)
    delta = relativedelta.relativedelta(d2,d1)
    print('How many years of investing?')
    print('%s years' % delta.years)
    number_of_years = delta.years
    print('Percentage of invest:')
    percent_invest = [0.25, 0.25, 0.25, 0.25]
    for i, x in zip(df.columns, percent_invest):
        cost = x * invested_amount
        print('{}: {}'.format(i, cost))
    print('Number of Shares:')
    percent_invest = [0.25, 0.25, 0.25, 0.25]
    for i, x, y in zip(df.columns, percent_invest, df.iloc[0]):
        cost = x * invested_amount
        shares = int(cost/y)
        print('{}: {}'.format(i, shares))
    print('Beginning Value:')
    percent_invest = [0.25, 0.25, 0.25, 0.25]
    for i, x, y in zip(df.columns, percent_invest, df.iloc[0]):
        cost = x * invested_amount
        shares = int(cost/y)
        Begin_Value = round(shares * y, 2)
        print('{}: ${}'.format(i, Begin_Value))
    print('Current Value:')
    percent_invest = [0.25, 0.25, 0.25, 0.25]
    for i, x, y, z in zip(df.columns, percent_invest, df.iloc[0], df.iloc[-1]):
        cost = x * invested_amount
        shares = int(cost/y)
        Current_Value = round(shares * z, 2)
        print('{}: ${}'.format(i, Current_Value))
    result = []
    percent_invest = [0.25, 0.25, 0.25, 0.25]
    for i, x, y, z in zip(df.columns, percent_invest, df.iloc[0], df.iloc[-1]):
        cost = x * invested_amount
        shares = int(cost/y)
        Current_Value = round(shares * z, 2)
        result.append(Current_Value)
    print('Total Value: $%s' % round(sum(result),2))
    future_value = round(sum(result),2)
    estimated_return = future_value - invested_amount
    response['status'] = True
    response['estimated_return'] = estimated_return
    return response
 

        



