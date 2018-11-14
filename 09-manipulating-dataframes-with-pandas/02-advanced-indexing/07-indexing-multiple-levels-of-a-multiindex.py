'''
Indexing multiple levels of a MultiIndex

Looking up indexed data is fast and efficient. And you have already seen that lookups based on the outermost level of a MultiIndex work just like lookups on DataFrames that have a single-level Index.

Looking up data based on inner levels of a MultiIndex can be a bit trickier. In this exercise, you will use your sales DataFrame to do some increasingly complex lookups.

The trickiest of all these lookups are when you want to access some inner levels of the index. In this case, you need to use slice(None) in the slicing parameter for the outermost dimension(s) instead of the usual :, or use pd.IndexSlice. You can refer to the pandas documentation for more details. For example, in the video, Dhavide used the following code to extract rows from all Symbols for the dates Oct. 3rd through 4th inclusive:

|   stocks.loc[(slice(None), slice('2016-10-03', '2016-10-04')), :]

Pay particular attention to the tuple (slice(None), slice('2016-10-03', '2016-10-04')).

INSTRUCTIONS

*   Look up data for the New York column ('NY') in month 1.
*   Look up data for the California and Texas columns ('CA', 'TX') in month 2.
*   Look up data for all states in month 2. Use (slice(None), 2) to extract all rows in month 2.
'''

import pandas as pd

sales = pd.read_csv('../datasets/sales.csv')

sales['state'] = ['CA', 'CA', 'NY', 'NY', 'TX', 'TX']
sales['month'] = [1, 2] * 3

sales = sales.set_index(['state','month'])

# ---

# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY', 1), :]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None),2), :]

'''
> sales
             eggs  salt  spam
state month                  
CA    1        47  12.0    17
      2       110  50.0    31
NY    1       221  89.0    72
      2        77  87.0    20
TX    1       132   NaN    52
      2       205  60.0    55

> NY_month1
eggs    221.0
salt     89.0
spam     72.0
Name: (NY, 1), dtype: float64

> CA_TX_month2
             eggs  salt  spam
state month
CA    2       110  50.0    31
TX    2       205  60.0    55

> all_month2
             eggs  salt  spam
state month
CA    2       110  50.0    31
NY    2        77  87.0    20
TX    2       205  60.0    55
'''