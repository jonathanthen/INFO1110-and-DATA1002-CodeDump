import pandas as pd

df = pd.read_csv('climate_data_Dec2017.csv')
group_state = df.groupby('State')
max_humid_group = group_state['9am relative humidity (%)'].max()
humid_dict = max_humid_group.to_dict()
for elem in humid_dict:
  print(elem + " : " + "{:.1f}".format(humid_dict[elem]))