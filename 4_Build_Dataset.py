import quandl
import pandas as pd

# UserKey to access API
api_key = "bNHUkRYjLghbbMsddUuM"

# Getting data for one US state
df = quandl.get('FMAC/HPI_AK', authtoken=api_key)
print(df.head())


# pd.read_html gets and returns all tables in the html as a list of DataFrames
us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

# Creating reference for all 50 US states
for abbv in us_states[0][1][1:].tolist():
    print("FMAC/HPI_"+str(abbv))
