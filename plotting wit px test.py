#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 27 07:34:52 2022

@author: konrad
"""

import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv('Validator_data_from_2022-04-04_until_2022-05-26.csv',index_col='Date',encoding='latin1')
data['Stake Balance']=data['Stake Balance'].astype(float)/1e18
data['Number of delegators']=data['Number of delegators'].astype(float)
data['Base Stake']=data['Base Stake'].astype(float)/1e18
data['Top up']=data['Top up'].astype(float)/1e18
data['Number of active nodes']=data['Number of active nodes'].astype(float)
data['Delegation cap']=data['Delegation cap'].astype(float)/1e18
data['Total number of nodes']=data['Total number of nodes'].astype(float)
data['locked']=data['locked'].astype(float)/1e18

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