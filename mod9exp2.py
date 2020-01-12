import pandas as pd

df = pd.read_csv('climate_data_Dec2017.csv')
max_wind_data = df['Speed of maximum wind gust (km/h)']
is_windy = max_wind_data > 60
windy_days = df[is_windy]
windy_days_high_temp = windy_days['Maximum temperature (C)']
mean_high_temp = windy_days_high_temp.mean()
print("Average max. temperature on windy days:", mean_high_temp)