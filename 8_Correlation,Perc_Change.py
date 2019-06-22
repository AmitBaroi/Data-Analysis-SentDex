"""
NOTE: Quandle now returns DataFrames with the DEFAULT:
index name: "Date" (Like before)
non-index column name = "Value" (!NEW!)
"""
import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# UserKey to access API
api_key = "bNHUkRYjLghbbMsddUuM"


def state_list():
    # pd.read_html gets and returns all tables in the html as a list of DataFrames
    us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return us_states[0][1][1:]


def grab_initial_state_data():
    states = state_list()
    # Empty DataFrame to add data
    main_df = pd.DataFrame()
    # Creating reference for all 50 US states
    for abbv in states:
        # Query for each states DataSet
        query = 'FMAC/HPI_'+str(abbv)
        # Getting each data sets
        df = quandl.get(query, authtoken=api_key)
        # Renaming columns to allow joining
        df.rename(columns={'Value': abbv}, inplace=True)
        print("\nGetting "+query+" . . .")
        # Converting HPI to Percent Change
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0
        print(df.head(2))
        print("Query complete!\n")

        # Filling in the empty DataFrame
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    # Showing a first few lines of our DataFrame
    print(main_df.head())

    # Saving DataFrame to file
    """Pickling: Serializes and saves the bytestream and we can load it back in fast and easily."""
    pickle_out = open('sav\states3.pickle', mode='wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    ################FUNCTION END#####################


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.columns = ["United States"]
    print(df.head())
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
    return df


fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('sav\states3.pickle')
benchmark = HPI_Benchmark()

HPI_data.plot(ax=ax1)
benchmark.plot(ax=ax1, color='k', linewidth=10)
plt.legend().remove()
print("\nClose plot to show correlation table.\n")
plt.show()

HPI_state_corr = HPI_data.corr()
print(HPI_state_corr)
print(HPI_state_corr.describe())

input("PRESS ENTER TO CLOSE")
