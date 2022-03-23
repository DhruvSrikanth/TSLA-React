import yfinance as yf

import data_settings as settings

import pandas as pd
from datetime import datetime

def get_data(look_back):
    
    data = yf.download(tickers=settings.TICKER, 
                    interval=settings.INTERVAL,
                    period=settings.PERIOD)

    data.reset_index(inplace=True)

    time = data.Datetime.tolist()[:-look_back]
    quote = data.Close.tolist()[:-look_back]

    data_dict = {"timestamp":time, 
                 "quote":quote}
    price_window = pd.DataFrame(data_dict)

    return price_window