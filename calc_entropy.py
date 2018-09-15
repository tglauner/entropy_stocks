import pandas as pd
import scipy as sc
import scipy.stats
import numpy as np

# Input a pandas series 
def ent(data):
    p_data= data.value_counts()/len(data) # calculates the probabilities
    entropy=sc.stats.entropy(p_data)  # input p robabilities to get the entropy 
    return entropy

ts = pd.Series(np.random.randint(0,100,size=100))
print ent(ts)
print ent(pd.Series(np.random.randint(0,100,size=1000)))

import json
import urllib2
url_aapl = 'https://api.iextrading.com/1.0/stock/aapl/chart/5y'
url_msft = 'https://api.iextrading.com/1.0/stock/msft/chart/5y'
pd_aapl = pd.read_json(url_aapl)
#print pd_apple
#print pd_apple['close']
print 'Entropy Apple = ', ent(pd_aapl['close'])
print 'Entropy MSFT = ', ent(pd.read_json(url_msft)['close'])