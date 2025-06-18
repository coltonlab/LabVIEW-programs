import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Load your Excel file
df = pd.read_excel('C:\\Data\\2025-06-04\\Raster Scan time.xlsx')

# Rename columns for ease of use
df.columns = ['Time_s', 'Captures', 'IntTime_ms', 'DarkSub', 'Average', 'TimeBetween_ms']

# Convert ms to seconds
df['IntTime_s'] = df['IntTime_ms'] / 1000
df['TimeBetween_s'] = df['TimeBetween_ms'] / 1000

# Compute time per capture
df['TimePerCapture'] = df['Time_s'] / df['Captures']

# Define inputs (X) and output (y)
X = df[['IntTime_s', 'DarkSub', 'Average', 'TimeBetween_s']]
y = df['TimePerCapture']

# Create regression model with interaction terms
poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
model = make_pipeline(poly, LinearRegression())

# Fit the model
model.fit(X, y)

# Extract model
reg = model.named_steps['linearregression']
features = poly.get_feature_names_out(X.columns)

# Display coefficients
print("Regression equation (TimePerCapture = ...):")
for name, coef in zip(features, reg.coef_):
    print(f"{name:20s}: {coef:.6f}")
print(f"{'Intercept':20s}: {reg.intercept_:.6f}")



import matplotlib.pyplot as plt

# Predict using the model
y_pred = model.predict(X)

# Plot actual vs predicted
plt.figure(figsize=(6, 6))
plt.scatter(y, y_pred, alpha=0.8, edgecolors='k')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', linewidth=2)  # 1:1 line
plt.xlabel("Actual Time per Capture (s)")
plt.ylabel("Predicted Time per Capture (s)")
plt.title("Actual vs Predicted Time per Capture")
plt.grid(True)
plt.tight_layout()
plt.show()
