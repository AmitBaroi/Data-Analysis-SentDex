import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Out Data:
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 34, 65, 56, 29, 76],
             'Bounce_Rate': [65, 67, 78, 65, 45, 52]}
df = pd.DataFrame(web_stats)
print(df.head())
print(df.tail(2))

# Replacing the default index(0,1...)
# Below both lines do the same thing!!!
# df = df.set_index('Day')                # Noob code
df.set_index("Day", inplace=True)       # Pro code
print(df.tail())

# Reference multiple columns with df[[col1, col2, ...]]
# Remember: DOUBLE SQUARE BRACKETS!!!
print(df[["Visitors", "Bounce_Rate"]])

# Plotting singe column
df["Visitors"].plot()
plt.legend()
plt.show()

# Plotting whole DataFrame
df.plot()
plt.show()
