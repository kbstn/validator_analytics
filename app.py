#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 26 13:24:45 2022

@author: kbstn
"""

# data needed: 
# daily data with mean values if there are multiple entrys for that day and no data if there ware no entrys
# columns:  Date            --> timestamp
#           Delegator APR   --> apr_y
#           Validator APR   --> apr_x
#           total stake     --> totalActiveStake,
#           base stake      --> stake,
#           stake percent   --> stakePercent,
#           Service Fee     --> serviceFee,
#           Delegation Cap  --> maxDelegationCap,
#           top up          --> topUp,
#           number of nodes --> validators,
#           identity        --> identity
#           name            --> name
#           fetured         --> featured,
#           explorerURL     -->
#           location
#           rank
#           locked
#           score
#           checkCapOnRedelegate
#           Delegators      --> numUsers
#           localtion


import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import create_plots
st.set_page_config(layout="wide")


st.title('Dashboard for analyzing validators of the Elrond Network')
st.write("""(*this is a prototype based on maually collected api data, DATA should not beed taken for granted. Also note that the api is treating 'legacy staking' not like a validator, thus some metrics on that might be missing )""")




# play arround with data
data = pd.read_csv('Validator_data_from_2022-04-04_until_2022-05-27.csv',index_col='Date',encoding='latin1')
data['Stake Balance']=data['Stake Balance'].astype(float)/1e18
data['Number of delegators']=data['Number of delegators'].astype(float)
data['Base Stake']=data['Base Stake'].astype(float)/1e18
data['Top up']=data['Top up'].astype(float)/1e18
data['Number of active nodes']=data['Number of active nodes'].astype(float)
data['Delegation cap']=data['Delegation cap'].astype(float)/1e18
data['Total number of nodes']=data['Total number of nodes'].astype(float)
data['Total Staked']=data['locked'].astype(float)/1e18



# distribution 

# silder over time

# users

# total staked
# datevar slider variable for all avail dates

st.subheader("Choose the parameter you are interested in, the selected validator will be highlighted, the silder will alter the barplots to the corresponding date")


left_column, middle_column,right_column = st.columns(3)
    
popertyvar = left_column.selectbox('Choose a parameter',[col for col in data.select_dtypes('float64').columns],index=4)

# select validator to highlight
var_validator = middle_column.selectbox(
     'Select a validator',
     [identity for identity in data.identity.unique()],index=43)


datevar = right_column.select_slider("Change the Date here", options=[date for date in data.index.unique()],value=data.index.max())


daily_data = data[data.index== datevar]





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



# plot decentralization

fig_ov_dec, ax = create_plots.plot_lorenz(daily_data,popertyvar)



#st.plotly_chart(fig_line, use_container_width=True)  


st.plotly_chart(fig_ov_property, use_container_width=True)  


st.subheader("")
st.subheader("Development of "+popertyvar+" over time validator "+var_validator+" is highlighted red")


# plot lines
df = data[['identity',popertyvar]]

hgihlight_line = create_plots.line_plot_highlight(df,var_validator,popertyvar)

st.plotly_chart(hgihlight_line, use_container_width=True) 


st.subheader("Gini coefficient and Lorenz curve, two measures to describe decentralization of a system")

    

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



# st.plotly_chart(fig_ov_stake, use_container_width=True)    
  
# next steps:
    
# 2 plots over time:
    # all validators in gray only multiselected in color
        # apr, fee, 
    # general network metrics over time
        # gini coeff, 


st.subheader("Investigate the raw data by your own")

st.write(data)