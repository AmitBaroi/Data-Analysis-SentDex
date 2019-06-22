import pandas as pd
"""
df1 and df3 have the same index, 
but they have some different columns. 
df2 and df3 have different indexes 
and some differing columns.
"""
df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])
df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])
# Concatenation works fine for dfs with same columns
con = pd.concat([df1, df2])
print(con)
# concat() adds dfs at the bottom, its a bit unorganized
con = pd.concat([df1, df2, df3])
print(con)

# Append
app = df1.append(df2)
print(app)
# Seems just like before
app = df1.append(df2).append(df3)
print(app)

"""
DataFrames are not really meant to be updated.
They are not to be treated like Databases.
Its more common to append a series to a DataFrame.
"""

# Making a Series object to append to df1
s = pd.Series([80, 2, 50], index=['HPI', "Int_rate", "US_GDP_Thousands"])
# Must set ignore_index True to append DataFrames (unless the series has a name)
ser = df1.append(s, ignore_index=True)
print(ser)
