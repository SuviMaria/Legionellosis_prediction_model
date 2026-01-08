## Legionellosis prediction model
Explore whether rainfall patterns can help explain or predict legionellosis case counts in Finland using time-series analysis and simple machine learning models

## Background
Legionnellosis shows strong seasonality trend all over the world. Seasonality has also grown stronger in Finland as shown in my bachelor's thesis. One of the strongest short time legionellosis rate predictors is the amount of rainfall and humidity as shown in various papers. (Fisman ym., 2005; Beauté ym., 2016) In this project my goal is to create a model that predicts the legionellosis rate in the following weeks in Finland based on the rainfall and humidity.

<img width="883" height="616" alt="image" src="https://github.com/user-attachments/assets/599ada1d-9e2c-44b9-b8f7-bebd253f2398" />

## Dataset
Dataset was created from publicly available data from THL and Ilmatieteen laitos. The weather data included data from four different measuring stations mainly in southern Finland as the population density is highest in the southern region of Finland. In the THL publicly available data, the cases are reported only on national level and for this reason the weather data was acquired mainly from the southern Finland. 

The assessed variables were monthly rainfall and monthly mean temperature as the combination of these two variables have an effect to the air humidity - an important legionellosis marker. 

The data was acquired from the following sources:
- THL, tartuntatautirekisteri, 2025
- Ilmatieteenlaitos, havaintojen lataus, 2025
    - Vantaa Helsinki-Vantaa lentoasema
    - Naantali, Raula
    - Kokkola, Öja Märskar
    - Luvia, Peränkylä
    - Kemiönsaari, Kemiö
    - Ruotsinpyhtää, Keitala
    - Hartola, Hotila
    - Tampere, Härmälä
    - Peräseinäjoki, Haukineva
    - Kerimäki, Yläkuona
    - Mäntyharju, Toivola
    - Mäntsälä, Hirvihaara
    - Lahti, Sopenkorpi
    - Kaarina Yltöinen
    - Oulu, Linnamaa
    - Juva, Partala


The data preprocessing steps included:
- Removing empty lines from both datasets
- In legionellosis dataset: 
    - Splitting the date line to year and month
    - Removing the lines that have all the cases of the year
    - Decoding the data to utf-8 format
    - Converting the months from Finnish names to ordinal numbers

The datasets were combined after cleaning and analyzed as pandas dataframes.

## Data analysis
The relationship between rainfall, monthly mean temperature and the incidence rate was assessed using Poisson regression, negative binomial regression and time-lag analysis. Both models were used with time-lag as the effect of rainfall likely doesn't show immediately. The model was tested using one, two and three month time lags. In a previous study the time lag for legionellosis cases was measured in weeks but as the publicly available data isn't available on weekly basis, months were used. The model was also tested with seasonality control. 

## Poisson regression:
- Assumes that the outcome follows a Poisson distribution
- Assumes variance = mean (equidispersion)
- Count data, non-negative discrete integer values
- Models log of expected count

## Negative binomial regression:
- Generalization of Poisson regression model
- Assumes variance > mean (overdispersion)




