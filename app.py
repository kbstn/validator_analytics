### outline for streamlit analytics dashboard

from numpy import identity
import streamlit

# get data from sqlite db (not late we will move to hosted msqldb)

# do all possible conversions in sql as a view

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
#           score
#           checkCapOnRedelegate
#           Delegators      --> numUsers
#           localtion

# select statement to get clean data from db
# select timestamp as 'Date',name,contract,apr_y as 'Delegator APR', apr_y as 'Validator APR',totalActiveStake as 'Stake Balance',
# stake as 'Base Stake',stakePercent as 'Stake percent',serviceFee as 'Service fee',maxDelegationCap as 'Delegation cap',
# topUp as 'Top up',validators as 'Number of active nodes',numNodes as 'Total number of nodes',numUsers as 'Number of delegators',identity,featured,explorerURL,location,rank,score,
# checkCapOnRedelegate as 'Check cap if full' from validators WHERE contract is not null and identity is not null