from numpy.random import seed
from numpy.random import randn
from numpy.random import lognormal
from scipy.stats import ks_2samp

#set seed (e.g. make this example reproducible)
seed(0)

#generate two datasets
nofeatures = [2050,2272,2000,2009,2167,2084,2091,2032,2350,2216 ]
featureOMSX30 = [1939,1995,2061,2100,2104,2034999,2438,2320,2418,2710]


#perform Kolmogorov-Smirnov test
print(ks_2samp(nofeatures, featureOMSX30))
