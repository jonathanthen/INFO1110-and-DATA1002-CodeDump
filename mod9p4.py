import pandas as pd

df = pd.read_csv('climate_data_Dec2017.csv')
is_26dec = df['Date'] == '2017-12-26'
filtered_date = df[is_26dec]

windf = df['Direction of maximum wind gust']
unique = pd.unique(pd.Series(windf))
unique = sorted(unique)

grouped_by_wind_dir = filtered_date.groupby('Direction of maximum wind gust')
group_sizes = grouped_by_wind_dir.size()
size_dict = group_sizes.to_dict()
for line in unique:
  if line not in size_dict:
    print(line + " : 0")
  else:
    print(line + " :",size_dict[line])
