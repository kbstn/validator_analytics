#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 07:34:52 2022

@author: kbstn
"""

import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv('Validator_data_from_2022-04-04_until_2022-05-26.csv',index_col='Date',encoding='latin1')
data['Stake Balance']=data['Stake Balance'].astype(float)/1e18
data['Number of delegators']=data['Number of delegators'].astype(float)
data['Base Stake']=data['Base Stake'].astype(float)/1e18
data['Top up']=data['Top up'].astype(float)/1e18
data['Number of active nodes']=data['Number of active nodes'].astype(float)
data['Delegation cap']=data['Delegation cap'].astype(float)/1e18
data['Total number of nodes']=data['Total number of nodes'].astype(float)
data['locked']=data['locked'].astype(float)/1e18
data['Service fee']=data['Service fee']/100
data['Number of delegators']=data['Number of delegators'].astype(float)

df= data[['Service fee','Validator APR','Delegator APR','Number of delegators']]


# # calulate man and std for every day. if reindexing results in nan (missing days)
# # then interpolate the data
# new_df['mean']=df.groupby('date').mean().reindex(pd.date_range(start=df.date.min(), end=df.date.max(), freq='D')).interpolate()
# new_df['SD']=df.groupby('date').std().reindex(pd.date_range(start=df.date.min(), end=df.date.max(), freq='D')).interpolate()
def group_by_date(dataframe):
    
     #group dataframe by column 'Date'
    grouped = dataframe.groupby('Date')
    
    #calculate mean and std for columns 'Service fee','Validator APR','Delegator APR'
    mean_service_fee = grouped['Service fee'].mean()
    
    std_service_fee = grouped['Service fee'].std()
    
    wght_mean_service_fee = (grouped['Service fee']* grouped['Number of delegators']).sum()/grouped['Number of delegators'].sum()

    mean_validator_apr = grouped['Validator APR'].mean()
    
    wght_mean_validator_apr = (grouped['Validator APR']* grouped['Number of delegators']).sum()/grouped['Number of delegators'].sum()

    std_validator_apr = grouped['Validator APR'].std()
    
    mean_delegator_apr = grouped['Delegator APR'].mean()
    
    wght_mean_delegator_apr = (grouped['Delegator APR']* grouped['Number of delegators']).sum()/grouped['Number of delegators'].sum()

    std_delegator_apr = grouped['Delegator APR'].std()
    
    #calculate sum for column 'Number of delegators'
    sum_delegators = grouped['Number of delegators'].sum()
    
    #create new dataframe with results
    results = pd.DataFrame({'mean service fee': mean_service_fee,
                           'std service fee': std_service_fee,
                           'weighted mean service fee': wght_mean_service_fee,
                           'mean validator apr': mean_validator_apr,
                           'std validator apr': std_validator_apr,
                           'weighted mean validator apr': wght_mean_validator_apr,

                           'mean delegator apr': mean_delegator_apr,
                           'std delegator apr': std_delegator_apr,
                           'weighted mean delegator apr': wght_mean_delegator_apr,

                           'sum delegators': sum_delegators})

    
    return results

result = group_by_date(df)
