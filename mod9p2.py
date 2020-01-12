import pandas as pd

df = pd.read_csv('climate_data_2017.csv')
max_temp = df['Maximum temperature (C)']
above_35 = max_temp > 35
max_temp_days = df[above_35]
rainfall_days = max_temp_days['Rainfall (mm)']
max_rainfall = rainfall_days.max()


print('Maximum amount of rainfall on hot days: {:.1f} mm'.format(max_rainfall))