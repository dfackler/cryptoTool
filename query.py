# https://blog.patricktriest.com/analyzing-cryptocurrencies-python/

import os
import numpy as np
import pandas as pd
import pickle
import quandl
from datetime import datetime

import plotly.offline as py
# import plotly.graph_objs as go
import plotly.graph_objs as go
import plotly.figure_factory as ff

# create function to retrieve bitcoin price data from Quandl
def get_quandl_data(quandl_id):
    '''Download and cache Quandl dataseries'''
    cache_path = '{}.pkl'.format(quandl_id).replace('/','-')
    try:
        f = open(cache_path, 'rb')
        df = pickle.load(f)   
        print('Loaded {} from cache'.format(quandl_id))
    except (OSError, IOError) as e:
        print('Downloading {} from Quandl'.format(quandl_id))
        df = quandl.get(quandl_id, returns="pandas")
        df.to_pickle(cache_path)
        print('Cached {} at {}'.format(quandl_id, cache_path))
    return df

# Pull Kraken BTC price exchange data
btc_usd_price_kraken = get_quandl_data('BCHARTS/KRAKENUSD')
# print(btc_usd_price_kraken.head())

# Chart the BTC pricing data
#py.sign_in('dfackler', '7KMQkbcwJhmnbkzutsL5')
# Scatter(x=btc_usd_price_kraken.index, y=btc_usd_price_kraken['Weighted Price'])
#py.image.save_as(btc_trace, filename='bitcoin.png')

# from IPython.display import Image
# Image('a-simple-plot.png')

trace = go.Bar(x=[2, 4, 6], y= [10, 12, 15])
data = [trace]
layout = go.Layout(title='A Simple Plot', width=800, height=640)
fig = go.Figure(data=data, layout=layout)

py.image.save_as(fig, filename='a-simple-plot.png')

from IPython.display import Image
Image('a-simple-plot.png')