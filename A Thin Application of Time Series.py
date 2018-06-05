# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 16:51:40 2018

@author: acarvalho
"""

# Import pandas and plotting modules
import pandas as pd
import matplotlib.pyplot as plt


#Time Series is assumed to be loaded from Google Trends
#TO DO: CREATE A script  to load this series into a Pandas DataFrame
# Convert the date index to datetime
diet.index = pd.to_datetime(diet.index)

# Plot 2012 data using slicing
diet['2012'].plot()
plt.show()

# Plot the entire time series diet and show gridlines
diet.plot(grid= True)
plt.show()