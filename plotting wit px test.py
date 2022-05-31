#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 07:34:52 2022

<<<<<<< HEAD
@author: kbstn
=======
@author: konrad
>>>>>>> first_outline
"""

import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
<<<<<<< HEAD
import numpy as np
=======
>>>>>>> first_outline

data = pd.read_csv('Validator_data_from_2022-04-04_until_2022-05-26.csv',index_col='Date',encoding='latin1')
data['Stake Balance']=data['Stake Balance'].astype(float)/1e18
data['Number of delegators']=data['Number of delegators'].astype(float)
data['Base Stake']=data['Base Stake'].astype(float)/1e18
data['Top up']=data['Top up'].astype(float)/1e18
data['Number of active nodes']=data['Number of active nodes'].astype(float)
data['Delegation cap']=data['Delegation cap'].astype(float)/1e18
data['Total number of nodes']=data['Total number of nodes'].astype(float)
data['locked']=data['locked'].astype(float)/1e18
<<<<<<< HEAD
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
=======

print([identity for identity in data.identity.unique()])
daily_data = data[data.index== data.index.max()]
var_validator=daily_data.identity.unique()[0]
popertyvar = 'locked'


default_color = "blue"
colors = {var_validator: "red"}


color_discrete_map = {
    c: colors.get(c, default_color) 
    for c in data.identity.unique()}

fig_ov_property = px.bar(daily_data.sort_values(by=[popertyvar],ascending=False),x='identity',y=popertyvar,color='identity',
               color_discrete_map=color_discrete_map)
fig_ov_property.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)'
})


var_validator = 'aerovek'
df = data[['identity','locked']]#

def line_plot_highlight(df,var_validator):
    df['Date'] = df.index
    
    fig = go.Figure()
    
        
    for validator in df.identity.unique():
        
        fig.add_trace(go.Scatter(x=df[df.identity == validator]['Date'], y=df[df.identity == validator]['locked'],line_color='lightgrey',mode='lines',name = validator))
    
    
    fig.add_trace(go.Scatter(x=df[df.identity == var_validator]['Date'], y=df[df.identity == var_validator]['locked'],line_color='red',line_width=4,mode='lines',name = var_validator))


    

    return fig

fig= line_plot_highlight(df,var_validator)
fig.show()
>>>>>>> first_outline
