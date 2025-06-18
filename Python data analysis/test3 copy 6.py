import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import PolynomialFeatures

# Load your Excel data
df = pd.read_excel('C:\\Data\\2025-06-04\\Raster Scan time.xlsx')
df.columns = ['Time_s', 'Captures', 'IntTime_ms', 'DarkSub', 'Average', 'TimeBetween_ms']

# Convert time to seconds
df['IntTime_s'] = df['IntTime_ms'] / 1000
df['TimeBetween_s'] = df['TimeBetween_ms'] / 1000
df['TimePerCapture'] = df['Time_s'] / df['Captures']

# Input features (X)
X_raw = df[['IntTime_s', 'DarkSub', 'Average', 'TimeBetween_s']]

# Add interaction terms
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
X_poly = poly.fit_transform(X_raw)
feature_names = poly.get_feature_names_out(X_raw.columns)

# Convert to DataFrame for statsmodels
X_df = pd.DataFrame(X_poly, columns=feature_names)
X_df = sm.add_constant(X_df)  # Adds intercept term

# Target (y)
y = df['TimePerCapture']

# Fit model with statsmodels
model = sm.OLS(y, X_df).fit()

# Print full summary with p-values
print(model.summary())
