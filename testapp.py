#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:24:45 2022

@author: konrad
"""
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import plot_decentralization
st.set_page_config(layout="wide")


st.title('Overview')



# play arround with data
data = pd.read_csv('Validator_data_from_2022-04-04_until_2022-05-26.csv',index_col='Date',encoding='latin1')
data['Stake Balance']=data['Stake Balance'].astype(float)/1e18
data['Number of delegators']=data['Number of delegators'].astype(float)
data['Base Stake']=data['Base Stake'].astype(float)/1e18
data['Top up']=data['Top up'].astype(float)/1e18
data['Number of active nodes']=data['Number of active nodes'].astype(float)
data['Delegation cap']=data['Delegation cap'].astype(float)/1e18
data['Total number of nodes']=data['Total number of nodes'].astype(float)



# distribution 

# silder over time

# users

# total staked
# datevar slider variable for all avail dates

datevar = st.sidebar.select_slider("Change the Date here", options=[date for date in data.index.unique()],value=data.index.max())

popertyvar = st.selectbox('What to show?',[col for col in data.select_dtypes('float64').columns],index=2)
daily_data = data[data.index== datevar]


fig_ov_stake =  px.histogram(daily_data['Stake Balance'],title="<b>Distribution of Stake balances</b>",#er Gender",  "day": "Day of Week", "total_bill": "Receipts"},
            # category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "sex": ["Male", "Female"]},
            # color_discrete_map={"Male": "RebeccaPurple", "Female": "MediumPurple"},
            template="simple_white"
            )

fig_ov_stake.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)'
})


fig_ov_property = px.bar(daily_data.sort_values(by=[popertyvar],ascending=False),x='identity',y=popertyvar)
fig_ov_property.update_layout({
'plot_bgcolor': 'rgba(0, 0, 0, 0)',
'paper_bgcolor': 'rgba(0, 0, 0, 0)'
})


# plot decentralization


fig_ov_dec, ax = plot_decentralization.plot_lorenz(daily_data,popertyvar)
# fig_ov_dec.set_size_inches(3,3)
left_column, middle_column,right_column = st.columns(3)

left_column.pyplot(fig_ov_dec)

right_column.image("https://miro.medium.com/max/1400/1*jOsIMe9ZTJLJFvfxJqddlQ.png")

middle_column.markdown("""In economics, the Lorenz curve is a graphical representation of the distribution of income or of wealth. 
                       It was developed by Max O. Lorenz in 1905 for representing inequality of the wealth distribution.
                       The curve is a graph showing the proportion of overall income or wealth assumed by the bottom x% 
                       of the people, although this is not rigorously true for a finite population (see below).
                       It is often used to represent income distribution, where it shows for the bottom x% of households,
                       what percentage (y%) of the total income they have. The percentage of households is plotted on the
                       x-axis, the percentage of income on the y-axis. It can also be used to show distribution of assets.
                       In such use, many economists consider it to be a measure of social inequality.
                       the concept is useful in describing inequality among the size of individuals in ecology[1]
                       and in studies of biodiversity, where the cumulative proportion of species is plotted against
                       the cumulative proportion of individuals.[2] It is also useful in business modeling:
                    e.g., in consumer finance, to measure the actual percentage y% of delinquencies attributable
                    to the x% of people with worst risk scores. """)


st.plotly_chart(fig_ov_property, use_container_width=True)  

st.plotly_chart(fig_ov_stake, use_container_width=True)    
  

