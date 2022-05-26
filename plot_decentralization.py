#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 15:01:26 2022

@author: konrad
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



def get_gini_coeff(array):
    """Calculate the Gini coefficient of a numpy array."""
    # based on bottom eq: http://www.statsdirect.com/help/content/image/stat0206_wmf.gif
    # from: http://www.statsdirect.com/help/default.htm#nonparametric_methods/gini.htm
    array = array.flatten() #all values are treated equally, arrays must be 1d
    if np.amin(array) < 0:
        array -= np.amin(array) #values cannot be negative
    array += 0.0000001 #values cannot be 0
    array = np.sort(array) #values must be sorted
    index = np.arange(1,array.shape[0]+1) #index per array element
    n = array.shape[0]#number of array elements
    return ((np.sum((2 * index - n  - 1) * array)) / (n * np.sum(array))) #Gini coefficient





def plot_lorenz(df,key,figsize=(6,6)):
    """
    plot lorenz curev with gini coefficient to show decentralization of data
    by giben key.
    needs a pandas dataframe as df and a str as column representation

    Parameters
    ----------
    df : TYPE
        DESCRIPTION.
    key : TYPE
        DESCRIPTION.

    Returns
    -------
    fig : TYPE
        DESCRIPTION.
    ax : TYPE
        DESCRIPTION.

    """
    
    # sort data by key column
    df = df.sort_values(by=[key],ascending=True)
    
    # drop null values and transorm selected key column to simple series
    data = df[df[key].notnull()][key].values
    
    # calculate the gini coefficient
    gini_coeff = get_gini_coeff(data)
    
    X_lorenz = data.cumsum() / data.sum()
    X_lorenz = np.insert(X_lorenz, 0, 0)
    
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ## scatter plot of Lorenz curve
    ax.scatter(np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz, 
               marker='x', color='b', s=2,label='Lorenz curve')
    plt.fill_between( np.arange(X_lorenz.size)/(X_lorenz.size-1), X_lorenz, color='blue', alpha=0.3)
    ## line plot of equality
    ax.plot([0,1], [0,1], color='k',label='Equality Line')
    
    # invisible plot to add gigi to label
    ax.plot([0,1], [0,1], color='k',alpha = 0,label='Gini coefficient: '+str(round(gini_coeff,2)))
    
    ax.legend()
    
    # set the labels for x, y, and title
    ax.set_xlabel("Entities")
    ax.set_ylabel("Distribution of "+key)
    ax.set_title("Decentralization of "+key+" (Lorenz Curve)") 
    
    fig.tight_layout()
    return fig,ax

# data = pd.read_csv('Validator_data_from_2022-04-04_until_2022-05-26.csv',index_col='Date',encoding='latin1')
# data['Stake Balance']=data['Stake Balance'].astype(float)/1e18
# data['Number of delegators']=data['Number of delegators'].astype(float)
# data['Base Stake']=data['Base Stake'].astype(float)/1e18
# data['Top up']=data['Top up'].astype(float)/1e18
# data['Number of active nodes']=data['Number of active nodes'].astype(float)
# data['Delegation cap']=data['Delegation cap'].astype(float)/1e18
# data['Total number of nodes']=data['Total number of nodes'].astype(float)
# # ensure your arr is sorted from lowest to highest values first!

# fig,ax=plot_lorenz(data,'Stake Balance')