import pandas as pd

df1 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]},
                   index=[2005, 2006, 2007, 2008])
df3 = pd.DataFrame({'HPI': [80, 85, 88, 85],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]},
                   index=[2001, 2002, 2003, 2004])
# Modified df1
df11 = pd.DataFrame({'Year': [2001, 2002, 2003, 2004],
                    'Int_rate': [2, 3, 2, 2],
                    'US_GDP_Thousands': [50, 55, 65, 55]})
# Modified df3
df33 = pd.DataFrame({'Year': [2001, 2003, 2004, 2005],
                    'Unemployment': [7, 8, 9, 6],
                    'Low_tier_HPI': [50, 52, 50, 53]})

# Merging dfs with same columns (but we loose index!)
print(pd.merge(df1, df2, on=['HPI', 'Int_rate', 'US_GDP_Thousands']))

# We need to set both dfs indexes the same
df1.set_index("HPI", inplace=True)
df3.set_index("HPI", inplace=True)
# Joining dfs with same index but no same columns
print(df1.join(df3))

# Merging dfs with no index and no same columns
"""
how = {left, right, outer, inner}

left:   merges keeping left df intact
right:  merges keeping right df intact
outer:  union of the dfs
inner:  intersection of the dfs          (DEFAULT)
"""
merged = pd.merge(df11, df33, on='Year', how='outer')
merged.set_index('Year', inplace=True)
print(merged)
