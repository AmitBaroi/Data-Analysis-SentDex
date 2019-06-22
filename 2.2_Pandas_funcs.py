import pandas as pd
import numpy as np

web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce_Rate': [65, 67, 78, 65, 45, 52]}
df = pd.DataFrame(web_stats)

# Referencing SINGLE Column
print(df['Bounce_Rate'])       # Slice notation
print(df.Bounce_Rate)          # Attribute notation

# Referencing MULTIPLE Columns
# Remember: DOUBLE SQUARE BRACKETS!!!
print(df[['Bounce_Rate', 'Day']])

# SINGLE column to list
print("\nVisitors to list:")
print(df.Visitors.tolist())
print(df['Bounce_Rate'].tolist())

# MULTIPLE columns to array
print("Bounce_Rate and Visitors to array:")
arr = np.array(df[['Bounce_Rate', 'Visitors']])
print(arr)

# Array to DataFrame
df2 = pd.DataFrame(arr)
print("Array to DataFrame:")
print(df2)



