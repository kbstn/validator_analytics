# only run local.
# get data from sqlite db
# do some tweak operations
# save as csv for later use in dashboard

import sqlite3
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import datetime
import matplotlib.ticker as ticker

def read_sqlite_db_into_pandas(db_file,query, parse_dates, index_col):
    """
    Reads sqlite db into a pandas dataframe
    """
    
    # connect to db
    conn = sqlite3.connect(db_file)
    
    # read db into pandas dataframe
    df = pd.read_sql_query(query, conn, 
                           parse_dates=parse_dates)
    
    # close connection to db
    conn.close()
    
    return df
    
    
def calculate_mean_percent_per_day(df):
    """
    Calculates the mean percent per day
    """
    
    # create a date column to better work with the dates
    df['Date']= df.Date.dt.date
    
    # as data is npot daily and contains gaps create a new index with entries for 
    # all days inbetween the first and last
    new_index = pd.date_range(start=df.Date.min(), end=df.Date.max(), freq='D')
    
    #create a empty df with new daily index to dump results in
    new_df =pd.DataFrame(index=new_index)
    # calulate man and std for every day. if reindexing results in nan (missing days)
    # then interpolate the data
    new_df['mean']=df.groupby('Date').mean().reindex(pd.date_range(start=df.Date.min(), end=df.Date.max(), freq='D')).interpolate()
    new_df['SD']=df.groupby('Date').std().reindex(pd.date_range(start=df.Date.min(), end=df.Date.max(), freq='D')).interpolate()
    return new_df
if __name__ == '__main__':
    
    # db file
    db_file = '/home/konrad/Nextcloud/projects/crypto/elrond/dolphinpool/validator_db/validators.db'
    
    # query
    query = """select timestamp as 'Date',name,contract,apr_y as 'Delegator APR', apr_y as 'Validator APR',totalActiveStake as 'Stake Balance',
                stake as 'Base Stake',stakePercent as 'Stake percent',serviceFee as 'Service fee',maxDelegationCap as 'Delegation cap',
                topUp as 'Top up',validators as 'Number of active nodes',numNodes as 'Total number of nodes',numUsers as 'Number of delegators',identity,featured,explorerURL,location,rank,score,
                checkCapOnRedelegate as 'Check cap if full' from validators WHERE contract is not null and identity is not null"""
    # parse dates
    parse_dates = ['Date']
    
    # index col
    index_col = 'Date'
    
    # read sqlite db into pandas dataframe
    df = read_sqlite_db_into_pandas(db_file, query, parse_dates, index_col)
    
    # nach timestamp gruppieren und mean und sd berrechen
    
    # get dates only
    mean= calculate_mean_percent_per_day(df)

    
    