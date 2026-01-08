"""
30.12.2025
Analysing the legionellosis data using Poisson regression and negative
binomial regression of the statsmodels library. As variance 
"""


import legionellosis_data_cleaning as data
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Checking variance and mean. As variance is greater,
# negative binomial chosen
print(data.df['rainfall_mm'].mean())
print(data.df['rainfall_mm'].var())

# Adding time lag
data.df['rain_lag_1'] = data.df['rainfall_mm'].shift(1)
data.df['rain_lag_2'] = data.df['rainfall_mm'].shift(2)
data.df['rain_lag_3'] = data.df['rainfall_mm'].shift(3)

# Removing NA-values
df = data.df.dropna().copy()

X = data.df[['rain_lag_1', 'rain_lag_2', 'rain_lag_3', 'mean_temp_c']] # Features as df
y = data.df['cases'] # Target as series

# Negative binomial
model_negative_bin = smf.negativebinomial(
    formula='cases ~ rainfall_mm + rain_lag_1 + rain_lag_2 + rain_lag_3 + mean_temp_c',
    data=df,
    family=sm.families.Poisson()
).fit()

print(model_negative_bin.summary())

# Negative binomial regression