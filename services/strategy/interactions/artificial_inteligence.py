
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
from datetime import datetime, timedelta
from dateutil import relativedelta

import yfinance as yf

def artificial_ineligence_strategy():
    response = {'status': False}
    current_probables = ['TATAELXSI.NS', 'PERSISTENT.NS', 'OFSS.NS']
    df = pd.DataFrame()
    for s in current_probables:
        df[s] = yf.download(s,period='2y')['Adj Close']

    d1 = datetime.now()
    d2 = datetime.now() + timedelta(weeks = 100)
    delta = relativedelta.relativedelta(d2,d1)
    print('How many years of investing?')
    print('%s years' % delta.years)
    number_of_years = delta.years
    days = (df.index[-1] - df.index[0]).days
    plt.figure(figsize=(12,8))
    plt.plot(df)
    plt.title('Artificial Intelligence Stocks Closing Price')
    plt.legend(labels=df.columns)
    normalize = (df - df.min())/ (df.max() - df.min())

    # for here we just go on to analyze graph and decide for ourself
        


