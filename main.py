import numpy as np
import pandas as pd

# Series object is a 1D array of indexed data
# Like a COLUMN (one category)
month = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(month)
# Series have attributes values & index
print(month.values) # looks like a list 
print(month.index) # shows the range of nums

# You can set the index explicitly!!!
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
better_month = pd.Series(month_list, index=[1,2,3,4,5,6,7,8,9,10,11,12])

# Access value at index
print(f'My birthday is in {better_month[1]}') 

# Can also think of Series like a simple dictionary with key:value pairs
birth_months = {'Kevin':'Mar',
                'Jackson':'Aug',
                'Finny':'Jul',
                'Bryce':'Nov',
                'Natalie':'Mar',
                'Paige':'Feb',
                'Maia':'Apr'}
birth_series = pd.Series(birth_months)
print(birth_series)

# Create a DataFrame from a single Series object
df = pd.DataFrame(birth_series, columns=['Birth Month'])
print(df) # DataFrame objects have column headers!

# Load tabular data from a CSV file into a DataFrame
pokemon_df = pd.read_csv('pokemon_data.csv')
print(pokemon_df) # [800 rows x 12 cols]
print(pokemon_df.columns) # display col headers

# Column headers can be used to access individual columns
print(pokemon_df['Name'])
# Shortcut using DOT OPERATOR notation
print(pokemon_df.HP)
# Shortcut does not work for all column names...
#print(pokemon_df.Type 1)
print(pokemon_df['Type 1'])

# Add a new column 
# Fill values with a calculation
pokemon_df['Attack Ratio'] = pokemon_df['Attack'] / pokemon_df['Sp. Atk']

# Examples of getting info about a DataFrame
print( pokemon_df.head(10) ) # show first n rows
print( pokemon_df.sample(3) ) # show random sample of n rows
print( pokemon_df.shape ) # returns a tuple ( rows, cols )
print( pokemon_df.columns ) # returns a list of column headers
print( pokemon_df.info() ) # shows non-null count & dtypes
print( pokemon_df.describe() ) # mean, std, min, max
print( pokemon_df['Defense'].describe() ) # stats for a specific col
print( pokemon_df['Type 1'].value_counts() ) # frequency of value counts

# How to locate specific rows
print( pokemon_df.loc[4] ) # gives you charmander

# groupby function helps you isolate groups of entries
print ( pokemon_df.groupby('Type 1')[[ 'HP', 'Speed'] ].mean() )
# similar to .value_counts
print ( pokemon_df.groupby('Type 1').size().sort_values() ) 
# Average combined stats by generation
pokemon_df['Total'] = pokemon_df[ ['HP', 'Attack', 'Defense', 'Speed'] ].sum(axis=1)
print( pokemon_df['Total'] )
# Which generation has the strongest pokemon?
print( pokemon_df.groupby('Generation')['Total'].mean() )
# Compare legendary pokemon to non-legendary
print( pokemon_df.groupby('Legendary')['Total'].mean() )

# CONDITIONAL FILTERING

# Select Pokemon with HP greater than 100
# Pulling ROWS (entries) where the value in the 'HP' COLUMN > 100
subset1 = pokemon_df[ pokemon_df['HP'] > 100 ]
# Select Poison-type
subset2 = pokemon_df[ pokemon_df['Type 1'] == 'Poison']
# Compound operators -> AND is &, OR is | for Pandas
# First condition: poison pokemon that are not also flying type
# Second condition: AND before gen 5
subset3 = subset2[ (subset2['Type 2'] != 'Flying') & (subset2['Generation'] < 5) ]
print(subset3)

# Select pokemon whose name contains "Mega"
subset4 = pokemon_df[ pokemon_df['Name'].str.contains('Mega') ]
print(subset4)

# Exclude Legendary Pokemon
subset5 = pokemon_df[ pokemon_df['Legendary'] == False ]
# OR you could do the same thing like this:
subset6 = pokemon_df[ ~pokemon_df['Legendary'] ]











