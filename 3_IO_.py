import pandas as pd

"""
Input: pd.read_csv, read_html etc.
Output: pd.to_csv, to_html etc.
"""

# Reading our downloaded data
df = pd.read_csv('data\ZILLOW-Z77006_HVI_Single_family.csv')
print(df.head())

# Setting index
df.set_index('Date', inplace=True)
# Saving the new DataFrame into a csv file
df.to_csv('sav/1_indexset.csv')
# Saving a single column into a csv file
df['Value'].to_csv('sav/2_value.csv')

df = pd.read_csv('sav/1_indexset.csv')
# Since csv dont have any attribute for index we loose index when we save to file
print('\nDamn the index is gone again!')
print(df.head())
# So here is the solution
df = pd.read_csv('sav/1_indexset.csv', index_col=0)
print('\nDataFrame with index set when loading file:')
print(df.head())

df = pd.read_csv('sav/1_indexset.csv')
# Changing column header names [Date->Date(Y-M-D), Values->House_Prices]
df.columns = ['Date(Y-M-D)', 'House_Prices']                      # This way we have to rename all columns
print("\nRenamed column headers")
print(df.head())

# Saving . . .
df.to_csv('sav/3_renamed_col.csv')
df.to_csv('sav/4_renamed_no_header.csv', header=False)
df = pd.read_csv('sav/4_renamed_no_header.csv')
print('\nReading header-less file . . .')
print(df.head())
# Reading new saved file, giving column header names and setting index to column 0
df = pd.read_csv('sav/4_renamed_no_header.csv', names=['Date', 'House_Price'], index_col=0)
print("\nReading header-less file . . .\ngiving header names and setting index to col 0:")
print(df.head())

# Saving to html . . .
df.to_html('sav/5_web.html')

# Reading and giving column header names
df = pd.read_csv('sav/4_renamed_no_header.csv', names=['Date', 'HPI'])
print(df.head())

# Renaming a single column
df.rename(columns={'HPI': 'Prices'}, inplace=True)
print(df.head())
