# -*- coding: utf-8 -*-
"""
Created on Mon May 30 09:40:42 2022

@author: bestiank
"""

import pandas as pd
import numpy as np

df = pd.read_csv(r'N:\4all.abt_n\User\Bestian\Validator_data_from_2022-04-04_until_2022-05-29.csv',
dtype={
'Date':str,
'contract':str,
'name':str,
'Delegator APR':float,
'Validator APR':float,
'Stake Balance':float,
'Base Stake':float,
'locked':float,
'Stake percent':float,
'Service fee':float,
'Delegation cap':float,
'Top up':float,
'Number of active nodes':int,
'Total number of nodes':float,
'Number of delegators':float,
'identity':str,
'featured':float,
'explorerURL':str,
'location':str,
'rank':int,
'score':int,
'Check cap if full':float})


# only one day
df.groupby(['Date','identity']).mean()


# interpolate gaps only if needed