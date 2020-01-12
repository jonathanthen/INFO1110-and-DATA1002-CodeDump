import pandas as pd

df = pd.read_csv('climate_data_Dec2017.csv')
is_humid_morning = df['9am relative humidity (%)'] > 60
humid_mornings = df[is_humid_morning]

grouped_by_state = humid_mornings.groupby('State')
rainfall_by_state = grouped_by_state['Rainfall (mm)']
max_rainfall_by_state = rainfall_by_state.max()

print("Maximum rainfall per state on humid days:")
print(max_rainfall_by_state.to_dict())