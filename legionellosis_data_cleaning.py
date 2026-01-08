"""
30.12.2025
Cleaning, normalizing, preprocessing and combining the legionellosis and 
weather data. The data is saved to pandas dataframe. 
The data cleaning includes:
    - Cleaning empty lines from both files
    - Decoding the data to utf-8 format in legionellosis dataset
    - Normalizing the months to ordinal numbers to match the weather dataset 
    in legionellosis dataset
    - Cleaning the lines that include the yearly compilation of cases in 
    legionellosis dataset
After preprocessing the dataframes are merged to one for analysis.
"""

import csv
import pandas as pd

# Helper function
def convert_month(month):
    """
    Convert a Finnish month name to its corresponding month number (1-12).

    Parameters
    ----------
    month : str
        Finnish month name (e.g. "tammikuu")

    Returns
    -------
    int
        Month number (1-12)
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


# Data saved from file to a list. Initialization.
weather_data = []
legionella_data = []  

# Opening and reading weather file contents
with open('/Users/suviketola/Desktop/Projektit/Legionellosis_prediction_project/rainfall_rain_1995-2025.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')

    for row in reader:

        # Cleaning lines that have the compilation text
        if row['Vuosi'] == "Vuosi":
            continue

        # Cleaning empty lines
        if row['Kuukauden keskilämpötila [°C]'] == "-":
            row['Kuukauden keskilämpötila [°C]'] = 0
        if row['Kuukauden sadesumma [mm]'] == "-":
            row['Kuukauden sadesumma [mm]'] = 0

        # Adding the data to list
        weather_data.append({
            'station': row['Havaintoasema'],
            'year': int(row['Vuosi']),
            'month': int(row['Kuukausi']),
            'rainfall_mm': float(row['Kuukauden sadesumma [mm]']),
            'mean_temp_c': float(row['Kuukauden keskilämpötila [°C]'])
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

        # Adding the data to the initialized list
        legionella_data.append({
            'year': year,
            'month': int(month_num),
            'cases': int(row['val'])
        })

# List converted to pandas dataframe
df_weather = pd.DataFrame(weather_data)
df_legionellosis = pd.DataFrame(legionella_data)

# New column "date" to use when calculating the mean rainfall and temperature for every month
df_weather["date"] = df_weather["year"].astype(str) + "-" + df_weather["month"].astype(str)

# Getting the mean rainfall and mean mean temperature for each month
monthly_df_weather = df_weather.groupby(["date"]).agg(rainfall_mm=("rainfall_mm", "mean"),
                                    mean_temp_c=("mean_temp_c", "mean"),
                                    month = ("month", "first"),
                                    year = ("year", "first"),
                                    date = ("date", "first"))

# Merging the weather and legionellosis dataframes
df = pd.merge(monthly_df_weather, df_legionellosis, on=['year', 'month'], how='outer')

print(df)