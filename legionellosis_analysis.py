# This project aims to assess the legionellosis incidence rate in Finland and
# create a model to predict the incidence rate based on rainfall and mean
# temperature of several measuring stations.

import csv
import pandas as pd

# Data saved to a list
weather_data = []

# Opening and reading file contents
with open('/Users/suviketola/Desktop/Projektit/Legionellosis_prediction_project/rainfall_rain_1995-2025.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')

    for row in reader:

        # Cleaning empty lines
        if row['Ilman keskilämpötila [°C]'] == "-":
            row['Ilman keskilämpötila [°C]'] = 0
        if row['Sademäärä [mm]'] == "-":
            row['Sademäärä [mm]'] = 0

        weather_data.append({
            'station': row['Havaintoasema'],
            'year': int(row['Vuosi']),
            'month': int(row['Kuukausi']),
            'day': int(row['Päivä']),
            'rainfall_mm': float(row['Sademäärä [mm]']),
            'mean_temp_c': float(row['Ilman keskilämpötila [°C]'])
        })

# List converted to panda
df = pd.DataFrame(weather_data)
print(df)
