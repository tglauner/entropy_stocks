import pandas as pd
import scipy as sc
import scipy.stats
import numpy as np
import json
import urllib2
import matplotlib.pyplot as plt

# Input a pandas series 
def ent(data):
    p_data= data.value_counts()/len(data) # calculates the probabilities
    entropy=sc.stats.entropy(p_data)  # input p robabilities to get the entropy 
    return entropy

def calc(ticker):
	url_ticker = 'https://api.iextrading.com/1.0/stock/'+ticker+'/chart/5y'
	#print url_ticker
	pd_ticker = pd.read_json(url_ticker)
	close_ticker = pd_ticker['close']
	print 'Entropy ',ticker,' = ', ent(close_ticker)
	close_ticker.plot()
	return url_ticker, pd_ticker, close_ticker

#Random numbers with same size as the stocks
print 'Entropy Random 1260 items: ', ent(pd.Series(np.random.randint(0,100,size=1260)))

calc('aapl')
calc('msft')
calc('banc')
calc('htbi')
calc('dhi')

plt.show(block=True)