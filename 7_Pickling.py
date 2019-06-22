import quandl
import pandas as pd
import pickle

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
        """ 
    Giving unique column names to each data frames 2nd column
    This is to prevent Value Error when joining (Columns Overlap: dfs have same column names)
    """
        df.rename(columns={'Value': abbv}, inplace=True)

        # Filling in the empty DataFrame
        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)
    # Showing a first few lines of our DataFrame
    print(main_df.head())
    """Pickling: Serializes and saves the bytestream and we can load it back in fast and easily."""
    pickle_out = open('sav\states.pickle', mode='wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


"""
We dont have to call the function since the data is pickled
# grab_initial_state_data()
"""

# Pickle module version
pickle_in = open('sav\states.pickle', mode='rb')
HPI_data = pickle.load(pickle_in)
print(HPI_data)

# Pandas module version
HPI_data.to_pickle('sav\pickle.pickle')
HPI_data2 = pd.read_pickle('sav\pickle.pickle')
print(HPI_data2)
