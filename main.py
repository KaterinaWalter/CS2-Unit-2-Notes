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
