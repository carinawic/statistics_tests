# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import random


heights = random.sample(range(130, 200), 10)

heights = [2050.4559343257447 , 2272.31859035583, 2000.5820620469208 
, 2009.1359669370624 , 2167.8426462840966, 2084.7494715645284, 2091.7702655493063, 2032.6512754284502 , 2350.5765626439006, 2216.6563842854785]
print("std: ", np.std(heights))
print("25-percentile: ", np.percentile(heights, 25))
print("mean: ", np.mean(heights))
print("median: ", np.median(heights))

heights_mean = np.mean(heights)

# Create a function to get x, y for of ecdf
def get_ecdf(data):
    """Returns x,y for ecdf"""
    # Get lenght of the data into n
    n = len(data)
    
    # We need to sort the data
    x = np.sort(data)
    
    # the function will show us cumulative percentages of corresponding data points
    y = np.arange(1,n+1)/n
    
    return x,y

# Create a function to plot ecdf
def plot_ecdf(data,labelx,labely,title,color):
    """Plot ecdf"""
    # Call get_ecdf function and assign the returning values
    x, y = get_ecdf(data)
    
    plt.plot(x,y,marker='.',linestyle='none',c=color)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.title(title)

def draw_bs_replicates(data,func,size):
    """creates a bootstrap sample, computes replicates and returns replicates array"""
    # Create an empty array to store replicates
    bs_replicates = np.empty(size)
    
    # Create bootstrap replicates as much as size
    for i in range(size):
        # Create a bootstrap sample
        bs_sample = np.random.choice(data,size=len(data))
        # Get bootstrap replicate and append to bs_replicates
        bs_replicates[i] = func(bs_sample)
    
    return bs_replicates

# Draw 15000 bootstrap replicates
bs_replicates_heights = draw_bs_replicates(heights,np.mean,15000) #15000
# Print empirical mean
print("Empirical mean: " + str(heights_mean))
# Print the mean of bootstrap replicates
print("Bootstrap replicates mean: " + str(np.mean(bs_replicates_heights)))

# # Plotting Empirical CDF
# plot_ecdf(heights,"Height (cm)","percentage","Empirical CDF","r")
# plt.show()

# sns.distplot(heights,hist=False)
# plt.xlabel("Height(cm)")
# plt.ylabel("PDF")
# plt.title("Probability Density Function")
# plt.show()

# weights = np.ones_like(bs_replicates_heights)/float(len(bs_replicates_heights))
# Plot the PDF for bootstrap replicates as histogram


# Get the corresponding values of 2.5th and 97.5th percentiles
conf_interval = np.percentile(bs_replicates_heights,[2.5,97.5])

# Print the interval
print("The confidence interval: ",conf_interval)



plt.hist(bs_replicates_heights,bins=30,density=True)


# Showing the related percentiles
#plt.axvline(x=np.percentile(heights,[2.5]), ymin=0, ymax=1,label='2.5th percentile',c='y')
#plt.axvline(x=np.percentile(heights,[97.5]), ymin=0, ymax=1,label='97.5th percentile',c='r')

plt.xlabel("RMSE")
plt.ylabel("PDF")
plt.title("Probability Density Function")
plt.legend()
plt.show()