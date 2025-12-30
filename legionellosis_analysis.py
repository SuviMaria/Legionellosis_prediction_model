# This project aims to assess the legionellosis incidence rate in Finland and
# create a model to predict the incidence rate based on rainfall and mean
# temperature of several measuring stations.

import legionellosis_data_cleaning as data


# Poisson regression
X = data.df[['rain_lag_1', 'rain_lag_2', 'rain_lag_3', 'mean_temp_c']] # Features as DataFrame
y = data.df['cases'] # Target as series


# Negative binomial regression

# Model to predict