# -*- coding: utf-8 -*-
# ## Topics in Pandas
# **Stats 507, Fall 2021**
#

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [If-Then](#If-Then)
# + [Time Delta](#Time-Delta)
# + [Sorting](#Sorting)

# ## If Then
# **Kailin Wang**
# **wkailin@umich.edu**

# modules: --------------------------------------------------------------------
import numpy as np
import pandas as pd
from os.path import exists

# ## Pandas `if-then`  idioms
# - The `if-then/if-then-else` idiom is a compact form of if-else that can be implemented to columns in `pd.DataFrame`
# - Expressed on one column, and assignment to another one or more columns
# - Use pandas where after you’ve set up a mask

df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)
df

# ## Pandas `if-then`  idioms
# - An `if-then` on one column

df.loc[df.AAA >= 5, "BBB"] = -1
df

# - An `if-then` with assignment to 2 columns:

df.loc[df.AAA >= 5, ["BBB", "CCC"]] = 1022
df

# ## Pandas `if-then`  idioms
# - Use pandas where after you’ve set up a mask

df_mask = pd.DataFrame(
    {"AAA": [True] * 4, "BBB": [False] * 4, "CCC": [True, False] * 2}
)
df.where(df_mask,1022)

# ## Pandas `if-then-else`  idioms
# - if-then-else using NumPy’s where()

df = pd.DataFrame(
    {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
)
df
df["logic"] = np.where(df["AAA"] > 5, "high", "low")
df

# ## Time Delta
# **Liuyu Tao**
# **liuyutao@umich.edu**

# ## Overview
# - Parsing
# - to_timedelta

# ## Parsing
# - There are several different methods to construct the Timeselta, below are the examples

# +
import pandas as pd
import datetime

# read as "string"
print(pd.Timedelta("2 days 3 minutes 36 seconds"))
# similar to "datetime.timedelta"
print(pd.Timedelta(days=2, minutes=3, seconds=36))
# specify the integer and the unit of the integer
print(pd.Timedelta(2.0025, unit="d"))
# -

# ## Sorting
# **Julia Weber- juliaweb@umich.edu**

# ## Sorting- About
# - Pandas has built in functions that allow the user to sort values in a column or index of a dataframe.
# - Sorting is important, as a user can look for patterns in the data and easily determine which observations have the highest/lowest values for a certain variable.

# ## sort_values() Function
# - The sort_values() function can be used to order rows of a dataframe by the values of a column.
# - Default sorts low to high. If we set ascending=False, sorts high to low.

# +
import pandas as pd

names = ["Julia", "James", "Andrew", "Sandy", "Joe"]
ages = [15, 18, 16, 30, 26]
test_df = pd.DataFrame({"name" : names, "age" : ages})
test_df.sort_values("age", ascending=False)
# -

# ## sort_index() Function
# - The sort_index() function can be used to sort the index of a dataframe.
# - This function is similar to the sort_values() function, but is applied to the index.

sorted_df = test_df.sort_values("age", ascending=False)
sorted_df.sort_index()
