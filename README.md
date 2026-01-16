## Legionellosis prediction 
Explore whether rainfall and temperature patterns can help explain or predict legionellosis case counts in Finland using time-series analysis and simple machine learning models

## Background
Legionnellosis shows strong seasonality trend all over the world. Seasonality has also grown stronger in Finland as shown in the graph I created for my bachelor thesis below. One of the strongest short time legionellosis rate predictors is the amount of rainfall and humidity as shown in various papers. (Fisman ym., 2005; Beauté ym., 2016) In this project my goal is to assess the legionellosis rate in the following months in Finland based on the rainfall and temperature.

<img width="883" height="616" alt="image" src="https://github.com/user-attachments/assets/599ada1d-9e2c-44b9-b8f7-bebd253f2398" />

## Dataset
Dataset was created from publicly available data from THL (Finnish institute for health and welfare) and Ilmatieteen laitos (Finnish meteorological institute). The weather data included data from four different measuring stations mainly in southern Finland as the population density is highest in the southern region of Finland. In the THL publicly available data, the cases are reported only on a national level and for this reason the weather data was acquired mainly from the southern Finland. 

The assessed variables were monthly rainfall and monthly mean temperature as the combination of these two variables have an effect to the air humidity which is an important legionellosis marker. 

An important limitation of the data is the underdiagnosis of legionellosis in Finland, as noted by THL. For this reason the data cannot create a completely trustworthy prediction model but it can help to increase the overall understanding on how the weather patterns effect the incidence rate in Finland.

The data was acquired from the following sources:
- THL, tartuntatautirekisteri, 2025 
    - Monthly cases from 1/1995-12/2025
- Ilmatieteenlaitos, havaintojen lataus, 
    - Following stations mean monthly temperature and rainfall: 
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

The datasets were combined after cleaning and analyzed as pandas dataframes. This resulted in 369 monthly observations.

## Data analysis
The relationship between rainfall, monthly mean temperature and the incidence rate was assessed using negative binomial regression and time-lag analysis. Poisson regression was also considered but due to overdispersion as variance > mean negative binomial regression model was used instead. Model was also used with time-lag as the effect of rainfall likely doesn't show immediately. The model was tested using one, two and three month time lags. In a previous study the time lag for legionellosis cases was measured in weeks but as the publicly available data isn't available on weekly basis, months were used. 

## Negative binomial regression:
- Generalization of Poisson regression model
- Assumes variance > mean (overdispersion)

## Results
The summary of results is given below:

<img width="616" height="409" alt="image" src="https://github.com/user-attachments/assets/7f08c8b5-f684-4160-a14b-4cccc3eef2c2" />

Based on the LLR p-value of 2.796e-08, the results can be considered reliable and based on the alpha value of 0.5434 there is overdispersion present in the data and thus negative binomial model was the best fit for this dataset.

Based on the results, the association between rainfall and legionellosis incidence rate is strongest in 2 and 3 month time lags. 1 month timelag has p-value of 0.152 and thus the result is not statistically significant. Strongest statistic significance with p-value of <0.001 was achieved with 3 month time lag. Thus the results could be summarized as rainfall 2-3 months earlier is associated with higher current legionellosis incidence rate with around 0.95% increase in current cases per 1 mm increase in rainfall in the previous 3 months. 

Statistically significant association between monthly mean temperature and legionellosis incidence rate was also found with p-value of 0.005. These results could be summarized as 2.3% increase in cases per 1°C increase in monthly mean temperature. This is consistent with literature and supports the seasonality of legionellosis cases where most cases are found during summer months.

In conclusion using a negative binomial regression to account for overdispersion, higher rainfall—particularly at 2–3 month lags—and higher mean temperature were associated with increased legionellosis incidence rates.
