# ## Pandas Topic
# Julia Weber- juliaweb@umich.edu

# ## Sorting
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


