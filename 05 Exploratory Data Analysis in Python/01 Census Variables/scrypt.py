# Census Variables
# You have decided to volunteer for your local community by offering to clean their recently collected census data.


# Import pandas with alias
import pandas as pd
# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
# View the first five rows of the DataFrame
print(census.head())

# Review: Based on .head(), 'birth_year' should be int, 'voted' is likely bool, 'num_children' is int, 'income_year' is float, 'higher_tax' and 'marital_status' are categorical.

# Fix data types
# Replace 'missing' in birth_year and convert to int
census['birth_year'] = census['birth_year'].replace('missing', 1967)
census['birth_year'] = census['birth_year'].astype('int64')
# Print the average birth year of the respondents
print(census['birth_year'].mean())

# View the first five rows of the DataFrame
print(census.head())
# View the values types for each column
print(census.dtypes)
# View the general description of the values for the DataFrame
print(census.describe(include = 'all'))


# Print the unique values of the 'higher_tax' using the .unique() method.
print(census['higher_tax'].unique())
census['higher_tax'] = pd.Categorical(census['higher_tax'], ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'])
# Print the unique values of the 'higher_tax' using the .unique() method.
print(census['higher_tax'].unique())

# Use cat.codes to label encode the higher_tax variable
census['higher_tax_label'] = census['higher_tax'].cat.codes
# Print the median code of the higher_tax variable
print(census['higher_tax_label'].median())
# Print the median value of the higher_tax variable
print(census['higher_tax'].unique()[int(census['higher_tax_label'].median())])

# One-Hot Encode marital_status to create binary variables of each category
census = pd.get_dummies(data=census, columns=['marital_status'])
# Print the first five rows of the new dataframe
print(census.head())
