# This project aims to assess the legionellosis incidence rate in Finland and
# create a model to predict the incidence rate based on rainfall and mean
# temperature of several measuring stations.

from calendar import c
import csv
import pandas as pd

# Helper function
def convert_month(month):
    """
    Convert a Finnish month name to its corresponding month number (1–12).

    Parameters
    ----------
    month : str
        Finnish month name (e.g. "tammikuu")

    Returns
    -------
    int
        Month number (1–12)
    """

    MONTH_MAP = {
    "tammikuu": 1,
    "helmikuu": 2,
    "maaliskuu": 3,
    "huhtikuu": 4,
    "toukokuu": 5,
    "kesäkuu": 6,
    "heinäkuu": 7,
    "elokuu": 8,
    "syyskuu": 9,
    "lokakuu": 10,
    "marraskuu": 11,
    "joulukuu": 12
    }

    return MONTH_MAP[month]


# Data saved to a list
weather_data = []
legionella_data = []  

# Opening and reading weather file contents
with open('/Users/suviketola/Desktop/Projektit/Legionellosis_prediction_project/rainfall_rain_1995-2025.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')

    for row in reader:

        # Cleaning empty lines
        if row['Ilman keskilämpötila [°C]'] == "-":
            row['Ilman keskilämpötila [°C]'] = 0
        if row['Sademäärä [mm]'] == "-":
            row['Sademäärä [mm]'] = 0

        # Adding the data
        weather_data.append({
            'station': row['Havaintoasema'],
            'year': int(row['Vuosi']),
            'month': int(row['Kuukausi']),
            'rainfall_mm': float(row['Sademäärä [mm]']),
            'mean_temp_c': float(row['Ilman keskilämpötila [°C]'])
        })

# Opening and reading legionellosis file contents
with open('/Users/suviketola/Desktop/Projektit/Legionellosis_prediction_project/legionellosis_cases.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')

    for row in reader:

        # Cleaning empty lines
        if row['val'] == "":
            row['val'] = 0

        # Splitting the time for month and year
        time = row['Aika'].split()
        month = time[0]
        year = int(time[1])

        # Cleaning lines that have yearly compilation by skipping
        if month == "Vuosi":
            continue

        # Decoding to utf-8
        month = month.encode("latin1").decode("utf-8")

        # Converting months to numbers from Finnish month names
        month_num = convert_month(month)

        legionella_data.append({
            'year': year,
            'month': int(month_num),
            'cases': int(row['val'])
        })

# List converted to panda
df_weather = pd.DataFrame(weather_data)
df_legionellosis = pd.DataFrame(legionella_data)

# Getting the mean rainfall and mean mean temperature for each month
monthly_df_weather = df_weather.groupby("month").agg(rainfall_mm=("rainfall_mm", "mean"),
                                    mean_temp_c=("mean_temp_c", "mean"), 
                                    station = ("station", "first"),
                                    year = ("year", "first"))