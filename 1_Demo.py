"""
Just Harrison Kinsley (SentDex) showing off what Python can do!

I made a few adjustments:
# morningstar API deprecated so I used yahoo.
# removed line "df = df.drop("Symbol", axis=1)", There is no such column
"""

import datetime
# pandas.io.data as web is no longer valid, so use this:
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# The date range of the data-set
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime.now()

# Getting stock data from a web API
df = web.DataReader("XOM", "yahoo", start, end)

# Resetting index to clear any unwanted index columns
df.reset_index(inplace=True)
# We will index by Date
df.set_index("Date", inplace=True)

# Showing the first 5 rows of data
print(df.head())

# Plotting
df['Close'].plot()
plt.legend()
plt.show()
