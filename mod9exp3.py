import pandas as pd

df = pd.read_csv('climate_data_Dec2017.csv')
grouped_by_wind_dir = df.groupby('Direction of maximum wind gust')
group_sizes = grouped_by_wind_dir.size()

print('Wind directions by number of days:')
print(group_sizes.to_dict())