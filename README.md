## Legionellosis prediction model
Explore whether rainfall patterns can help explain or predict legionellosis case counts in Finland using time-series analysis and simple machine learning models

## Background
Legionnellosis shows strong seasonality trend all over the world. Seasonality has also grown stronger in Finland as shown in my bachelor's thesis. One of the strongest short time legionellosis rate predictors is the amount of rainfall and humidity as shown in various papers. (Fisman ym., 2005; Beauté ym., 2016) In this project my goal is to create a model that predicts the legionellosis rate in the following weeks in Finland based on the rainfall and humidity.

<img width="883" height="616" alt="image" src="https://github.com/user-attachments/assets/599ada1d-9e2c-44b9-b8f7-bebd253f2398" />

## Dataset
Dataset was created from publicly available data from THL and Ilmatieteen laitos. The weather data included data from four different measuring stations mainly in southern Finland as the population density is highest in the southern region of Finland. In the THL publicly available data, the cases are reported only on national level and for this reason the weather data was acquired mainly from the southern Finland.

The data was acquired from the following sources:
- THL, tartuntatautirekisteri, 2025
- Ilmatieteenlaitos, havaintojen lataus, 2025
    - Vaasa Palosaari
    - Kuopio Maaninka
    - Pirkkala-Tampere lentoasema
    - Vantaa Helsinki-Vantaa lentoasema
