import pandas as pd
import scipy as sc
import scipy.stats
import numpy as np

# Input a pandas series 
def ent(data):
    p_data= data.value_counts()/len(data) # calculates the probabilities
    entropy=sc.stats.entropy(p_data)  # input probabilities to get the entropy 
    return entropy

ts = pd.Series(np.random.randint(0,100,size=100))
print ent(ts)
print ent(pd.Series(np.random.randint(0,100,size=1000)))
print ent(pd.Series(np.random.randint(0,100,size=10000)))
print ent(pd.Series(np.random.randint(0,100,size=100000)))
print ent(pd.Series(np.random.randint(0,100,size=1000000)))
