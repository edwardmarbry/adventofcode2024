
# %% [markdown]
##pandas read tsv file
import pandas as pd

# %%
df = pd.read_csv('day1input.csv', sep='|')

# put columns in separate dataframes
df1 = df['list1'].to_frame()
df2 = df['list2'].to_frame()

df1.sort_values(by='list1', inplace=True)
df1.reset_index(drop=True, inplace=True)

df2.sort_values(by='list2', inplace=True)
df2.reset_index(drop=True, inplace=True)


total_dist = df1['list1'].sub(df2['list2']).abs().sum()

print(total_dist)


# %%

import pandas as pd

def calculate_total_distance(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))
    
    return total_distance

def read_csv_and_calculate_distance(file_path):
    df = pd.read_csv('day1input.csv', sep='|')

    left_list = df['list1'].to_list()
    right_list = df['list2'].to_list()
    
    return calculate_total_distance(left_list, right_list)

file_path = 'day1input.csv'  
total_distance = read_csv_and_calculate_distance(file_path)
print(f"Total Distance: {total_distance}")


# %%
